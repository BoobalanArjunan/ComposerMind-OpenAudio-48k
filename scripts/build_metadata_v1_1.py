#!/usr/bin/env python3
"""Generate versioned acoustic metadata from audited final WAVs, without modifying originals."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

FIELDS = ("peak_dbfs", "rms_dbfs", "crest_factor_db")

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", type=Path)
    ap.add_argument("--measurements", type=Path, default=Path("validation/reports/acoustic_measurements.csv"))
    ap.add_argument("--output", type=Path, default=Path("validation/reports/metadata_v1.1.csv"))
    args = ap.parse_args()
    dataset = args.dataset.expanduser().resolve()
    source = dataset / "metadata.csv"
    output = args.output.expanduser().resolve()
    measurement_file = args.measurements.expanduser().resolve()
    if not source.is_file() or not measurement_file.is_file():
        ap.error("Missing metadata.csv or acoustic_measurements.csv; run validate_acoustics.py first")
    if output == source or output == measurement_file or output == dataset or dataset in output.parents:
        ap.error("Output must not overwrite source files or be inside dataset folder")
    with source.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        rows = list(reader)
    if not columns or any(c not in columns for c in ("file_name", *FIELDS)):
        ap.error("Metadata lacks required columns")
    with measurement_file.open(newline="", encoding="utf-8-sig") as f:
        measured = list(csv.DictReader(f))
    source_names = [r["file_name"] for r in rows]
    measured_names = [r["file_name"] for r in measured]
    if len(set(source_names)) != len(source_names) or len(set(measured_names)) != len(measured_names):
        ap.error("Duplicate filenames found; refusing to create versioned metadata")
    if set(source_names) != set(measured_names):
        ap.error("Filename mismatch between metadata and measurements")
    by_name = {r["file_name"]: r for r in measured}
    for row in rows:
        filename = row["file_name"]
        audio_path = dataset / filename
        if not audio_path.is_file():
            ap.error(f"Audio file missing: {filename}")
        m = by_name[filename]
        for key in FIELDS:
            try:
                float(m[key])
            except (ValueError, TypeError, KeyError):
                ap.error(f"Invalid measurement for {filename}: {key}")
            row[key] = str(m[key])
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        ap.error(f"Output already exists: {output}; move it first if regenerating")
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    report = {
        "version": "1.1",
        "original_metadata_sha256": sha256(source),
        "measurements_sha256": sha256(measurement_file),
        "output_metadata_sha256": sha256(output),
        "rows": len(rows),
        "modified_fields": list(FIELDS),
        "preserved_fields": [c for c in columns if c not in FIELDS],
        "method": "Full-track sample peak, stereo-combined sample RMS, and their difference; see scripts/validate_acoustics.py",
        "note": "Only acoustic fields updated. BPM, key, harmonic ratio and text descriptions have not been independently validated."
    }
    provenance = output.with_suffix(".provenance.json")
    provenance.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Created {output}")
    print(f"Created {provenance}")
    print(f"Rows: {len(rows)}; updated columns: {', '.join(FIELDS)}")
    print("Original metadata.csv and WAV files unchanged.")

if __name__ == "__main__":
    main()
