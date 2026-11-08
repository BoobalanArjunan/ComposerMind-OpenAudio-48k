# Metadata review — preliminary

Source: user-provided `metadata(1).csv` (94 rows, 27 columns). Review date: 2026-11-08.

## Verified from CSV content

- 94 rows, 94 unique `track_id` values, and 94 unique `file_name` values.
- No empty cells detected by CSV parsing.
- All rows report sample rate 48,000 Hz, 2 channels and 16-bit depth. **Audio files were not supplied for verification.**
- `primary_genre`, `sub_genre` and `mood_label` are constant across all rows. Keep as contextual tags, not independent classification labels.
- `harmonic_ratio` and `percussive_ratio` sum to 100 in each row. Their estimation method and meaning still need documentation.
- The `bpm_confidence` values are unusually concentrated at 99.4, but there is no documented estimator or calibration. Do not treat them as verified probabilities.
- `groove_quantization` has no documented units or computation method.
- `text_prompt` is a formulaic descriptive sentence built from track attributes; it is not established to be an actual music-generation prompt.
- `record_label` duplicates `publisher` across all rows; `musical_scale` repeats major/minor information contained in `musical_key`.
- Original CSV asserts CC-BY-4.0 for all tracks, but composition, recording and sample rights have not been independently verified.

## Proposed 23-column release metadata

**Remove** `record_label` (redundant), `musical_scale` (derivable), `bpm_confidence` (method unverified), and `groove_quantization` (definition unverified).

**Rename** `text_prompt` to `track_description` without changing its text.

**Temporarily replace** `license` values with `PENDING_RIGHTS_REVIEW` in the reviewed draft. This is an editorial safety flag, not a license grant. Restore a license identifier only after rights confirmation.

All remaining columns are preserved, including `harmonic_ratio`, `percussive_ratio`, `crest_factor_db`, `peak_dbfs` and `rms_dbfs`, but these are **unverified measurements** until recalculated from WAV files. The declared bit depth also needs verification.

## Required next checks

1. Compare the 94 actual WAV basenames against the 94 `file_name` values.
2. Check technical file properties, durations and audio fingerprints.
3. Independently recalculate and compare peak/RMS and other numerical features.
4. Document algorithm versions and units for tempo, key, harmonic/percussive analysis and crest factor.
5. Check key-to-Camelot mapping and any outliers.
6. Confirm ownership and third-party sample/voice rights, then approve a redistribution license.
7. Review descriptions for claims unsupported by listening or objective analysis.

**No audio was modified. No automated audio corrections or ground-truth validation have been performed.**
