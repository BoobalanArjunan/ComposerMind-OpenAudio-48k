#!/usr/bin/env python3
"""Non-destructive OpenAudio-48k WAV and metadata inventory audit. Standard library only."""
import argparse
import csv
import hashlib
import json
import struct
import wave
from collections import Counter
from pathlib import Path

def wav_info(path):
    try:
        with wave.open(str(path), "rb") as w:
            rate = w.getframerate()
            frames = w.getnframes()
            return {"sample_rate": rate, "channels": w.getnchannels(),
                    "sample_width_bits": w.getsampwidth() * 8,
                    "frames": frames, "duration_seconds": round(frames / rate, 6) if rate else None,
                    "compression": w.getcomptype(), "decode_status": "ok"}
    except (wave.Error, EOFError, OSError, ValueError, struct.error) as exc:
        return {"decode_status": "error", "error": str(exc)}

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("dataset", type=Path, help="Folder containing audio and metadata")
    p.add_argument("--output", type=Path, default=Path.cwd() / "validation" / "reports")
    p.add_argument("--hash", action="store_true", help="Calculate SHA256 for every WAV (slower)")
    args = p.parse_args()
    root = args.dataset.expanduser().resolve()
    out = args.output.expanduser().resolve()
    if not root.is_dir():
        p.error(f"Dataset folder not found: {root}")
    if out == root or root in out.parents:
        p.error("Output must be outside the dataset folder to keep source data untouched")
    wavs = sorted(x for x in root.rglob("*") if x.is_file() and x.suffix.lower() == ".wav")
    records = []
    for f in wavs:
        rec = {"relative_path": str(f.relative_to(root)), "filename": f.name,
               "size_bytes": f.stat().st_size, **wav_info(f)}
        if args.hash:
            rec["sha256"] = sha256(f)
        records.append(rec)
    csv_files = sorted(x for x in root.rglob("*") if x.is_file() and x.suffix.lower() == ".csv")
    metadata = []
    for f in csv_files:
        item = {"relative_path": str(f.relative_to(root))}
        try:
            with f.open("r", encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream)
                item["columns"] = reader.fieldnames or []
                rows = list(reader)
                item["row_count"] = len(rows)
                item["blank_values_by_column"] = {col: sum(not (row.get(col) or "").strip() for row in rows) for col in item["columns"] if col}
                item["sample_rows"] = rows[:2]
        except (OSError, UnicodeError, csv.Error) as exc:
            item["error"] = str(exc)
        metadata.append(item)
    filename_counts = Counter(f.name.casefold() for f in wavs)
    rates = Counter(str(x.get("sample_rate", "error")) for x in records)
    issues = []
    if len(wavs) != 94:
        issues.append(f"Expected 94 WAV files; found {len(wavs)}")
    for rec in records:
        if rec.get("decode_status") != "ok":
            issues.append(f"Unreadable/unsupported WAV: {rec['relative_path']}: {rec.get('error')}")
        elif rec.get("sample_rate") != 48000:
            issues.append(f"Not 48 kHz: {rec['relative_path']} ({rec['sample_rate']} Hz)")
    for name, count in filename_counts.items():
        if count > 1:
            issues.append(f"Repeated basename in multiple folders: {name} ({count} files)")
    hashes = Counter(x["sha256"] for x in records if "sha256" in x)
    for digest, count in hashes.items():
        if count > 1:
            issues.append(f"Identical file content SHA256 {digest}: {count} files")
    report = {"dataset_folder": str(root), "wav_count": len(wavs),
              "sample_rate_counts": dict(rates), "metadata_csv_files": metadata,
              "issues": issues, "notes": [
                  "CSV rows are inventoried but not automatically matched to audio: schema must be reviewed first.",
                  "Python wave supports standard PCM WAV; other WAV encodings may require a separate decoder.",
                  "No source files were modified."
              ]}
    out.mkdir(parents=True, exist_ok=True)
    (out / "audit_summary.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    columns = ["relative_path", "filename", "size_bytes", "decode_status", "sample_rate",
               "channels", "sample_width_bits", "frames", "duration_seconds", "compression", "error", "sha256"]
    with (out / "audio_manifest.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    print(f"WAV files: {len(wavs)} | CSV files: {len(csv_files)} | Issues: {len(issues)}")
    print(f"Reports: {out}")
    for issue in issues[:25]:
        print(" -", issue)
    if len(issues) > 25:
        print(f" ... and {len(issues)-25} more issues")

if __name__ == "__main__":
    main()
