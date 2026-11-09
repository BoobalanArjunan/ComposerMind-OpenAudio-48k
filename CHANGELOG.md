# Changelog

## Planned v1.1 — acoustic metadata correction

- Recompute `peak_dbfs`, `rms_dbfs`, and `crest_factor_db` directly from the 94 released final WAV files.
- Preserve all other metadata fields and the original audio unchanged.
- Save a separate `metadata_v1.1.csv` and hash-based provenance record.
- Document 252 discrepancies detected against original acoustic annotations (94 RMS, 94 crest factor, 64 peak), with a Track 01 independent FFmpeg cross-check.
- Original extraction code is unavailable; discrepancy cause remains unresolved.
- **Not yet published as a replacement to the Hugging Face dataset.** The new file must be generated locally and reviewed first.

## v1.0 — initial public release

- 94 stereo, 48 kHz, 24-bit WAV tracks and initial metadata.
