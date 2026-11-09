#!/usr/bin/env python3
"""Read-only block-streamed acoustic audit for OpenAudio-48k (NumPy + SoundFile)."""
import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
import soundfile as sf

EPS = 1e-15
BLOCK = 262144

def dbfs(x):
    return 20.0 * math.log10(max(float(x), EPS))

def analyze(path):
    peak = 0.0
    sum_sq = 0.0
    count = 0
    near_full_scale = 0
    exact_full_scale = 0
    silent_samples = 0
    with sf.SoundFile(str(path), mode="r") as wav:
        samplerate = wav.samplerate
        channels = wav.channels
        subtype = wav.subtype
        frames = len(wav)
        for block in wav.blocks(blocksize=BLOCK, dtype="float64", always_2d=True):
            absolute = np.abs(block)
            peak = max(peak, float(absolute.max(initial=0.0)))
            sum_sq += float(np.sum(block * block, dtype=np.float64))
            count += block.size
            near_full_scale += int(np.count_nonzero(absolute >= 0.999))
            exact_full_scale += int(np.count_nonzero(absolute >= 1.0))
            silent_samples += int(np.count_nonzero(absolute == 0.0))
    rms = math.sqrt(sum_sq / count) if count else 0.0
    return {
        "sample_rate": samplerate, "channels": channels, "subtype": subtype,
        "duration_seconds": round(frames / samplerate, 6) if samplerate else 0,
        "peak_dbfs": round(dbfs(peak), 4), "rms_dbfs": round(dbfs(rms), 4),
        "crest_factor_db": round(dbfs(peak) - dbfs(rms), 4),
        "near_full_scale_samples": near_full_scale,
        "exact_full_scale_samples": exact_full_scale,
        "zero_samples": silent_samples,
        "sample_values": count
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--output", type=Path, default=Path.cwd() / "validation" / "reports")
    args = parser.parse_args()
    root = args.dataset.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Dataset not found: {root}")
    if output == root or root in output.parents:
        parser.error("Output directory must be outside the dataset")
    metadata_path = root / "metadata.csv"
    if not metadata_path.is_file():
        parser.error(f"Missing metadata CSV: {metadata_path}")
    with metadata_path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    results = []
    issues = []
    for i, row in enumerate(rows, 1):
        filename = row["file_name"]
        matches = [p for p in root.rglob("*") if p.is_file() and p.name == filename]
        if len(matches) != 1:
            issues.append({"file_name": filename, "issue": f"Expected exactly one WAV, found {len(matches)}"})
            continue
        try:
            measured = analyze(matches[0])
        except Exception as exc:
            issues.append({"file_name": filename, "issue": f"Cannot decode: {exc}"})
            continue
        result = {"file_name": filename, **measured}
        for col in ("peak_dbfs", "rms_dbfs", "crest_factor_db"):
            try:
                declared = float(row[col])
                delta = round(measured[col] - declared, 4)
                result[f"metadata_{col}"] = declared
                result[f"delta_{col}"] = delta
                if abs(delta) > 0.5:
                    issues.append({"file_name": filename, "issue": f"{col} difference exceeds 0.5 dB", "delta_db": delta})
            except (ValueError, TypeError, KeyError):
                issues.append({"file_name": filename, "issue": f"Missing or invalid {col}"})
        if measured["near_full_scale_samples"]:
            issues.append({"file_name": filename, "issue": "Near-full-scale samples detected (not proof of clipping)", "count": measured["near_full_scale_samples"]})
        if measured["sample_values"] and measured["zero_samples"] == measured["sample_values"]:
            issues.append({"file_name": filename, "issue": "Entire track is digital silence"})
        results.append(result)
        print(f"[{i}/{len(rows)}] {filename}: peak {measured['peak_dbfs']:.2f}, RMS {measured['rms_dbfs']:.2f} dBFS")
    output.mkdir(parents=True, exist_ok=True)
    fields = ["file_name", "sample_rate", "channels", "subtype", "duration_seconds",
              "peak_dbfs", "rms_dbfs", "crest_factor_db",
              "metadata_peak_dbfs", "delta_peak_dbfs", "metadata_rms_dbfs", "delta_rms_dbfs",
              "metadata_crest_factor_db", "delta_crest_factor_db",
              "near_full_scale_samples", "exact_full_scale_samples", "zero_samples", "sample_values"]
    with (output / "acoustic_measurements.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)
    report = {"tracks_in_metadata": len(rows), "tracks_measured": len(results),
              "issues": issues,
              "methodology": {
                  "peak": "20 log10(max absolute sample value), all channels",
                  "rms": "20 log10(sqrt(mean(sample^2))), all channels and samples",
                  "crest_factor": "measured peak dBFS minus measured RMS dBFS",
                  "near_full_scale": "count of sample values with absolute magnitude >= 0.999",
                  "warning": "Sample peak is not true peak; near-full-scale samples do not prove audible clipping. Loudness (LUFS), silence segments, and semantic labels are not tested."
              }}
    (output / "acoustic_summary.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Measured {len(results)}/{len(rows)} tracks; findings: {len(issues)}")
    print(f"Reports: {output / 'acoustic_measurements.csv'} and {output / 'acoustic_summary.json'}")

if __name__ == "__main__":
    main()
