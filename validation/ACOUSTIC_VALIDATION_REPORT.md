# Acoustic validation report — OpenAudio-48k

## Scope and current status

The local dataset audit reported 94 readable WAVs, all 48,000 Hz, 24-bit, stereo, totaling 3.8849 hours. The metadata CSV contains 94 rows and 23 populated columns. Filename matching was 94/94, with no duration discrepancies above 0.1 seconds.

A subsequent full-file acoustic measurement pass analyzed all 94 WAVs and raised **252 metadata discrepancy flags**: 94 RMS, 94 crest-factor and 64 sample-peak differences exceeding 0.5 dB. These are *measurement discrepancies*, not 252 damaged audio files.

All 94 measured sample peaks were approximately −1.00 dBFS. The report did not flag any sample values at or above the near-full-scale threshold of 0.999, nor any wholly silent tracks. This does not establish absence of intersample true-peak clipping or all other defects.

## Independent cross-check

For Track 01, the original CSV states peak −0.70 dBFS, RMS −17.77 dBFS, and crest factor 17.07 dB. The Python audit measured approximately −1.00 dBFS peak and −13.62 dBFS RMS. FFmpeg astats (overall stereo result) independently reported peak −1.000001 dB and RMS −13.624322 dB. The two independent measurements agree within rounding.

The original BeatMind AI / TempoMind measurement implementation is unavailable. The original system reportedly analyzed these same final WAV files, so the discrepancy cannot currently be attributed to a different mastering version. Its exact cause remains unknown.

## Measurement definitions

- **Sample peak dBFS:** 20 × log10(maximum absolute decoded sample across both channels).
- **Full-track RMS dBFS:** 20 × log10(sqrt(mean(square of all decoded samples across both channels))).
- **Crest factor dB:** sample peak dBFS minus full-track RMS dBFS.
- **Flag threshold:** absolute difference greater than 0.5 dB between the original CSV value and independently measured value.
- **Near-full-scale screen:** counts decoded sample magnitudes at or above 0.999; this is not a true-peak or audible-distortion test.

## Metadata v1.1 procedure

Run `scripts/validate_acoustics.py` against the final WAV directory, then `scripts/build_metadata_v1_1.py`. The latter writes a **new CSV** outside the dataset, replacing only `peak_dbfs`, `rms_dbfs`, and `crest_factor_db` using measured values. The original metadata and WAV files are not modified. A provenance JSON file records hashes of the original metadata, measurements and output.

The v1.1 CSV should be reviewed and released as a versioned correction, not silently substituted for the published metadata. If uploaded to Hugging Face, update its dataset card and changelog and retain the original as an archived release.

## Remaining work

Independent BPM and key reference-label evaluation, harmonic/percussive annotation methodology, text-prompt quality, sample true peak, integrated loudness (LUFS), and rights/provenance checks are **not complete**. Do not claim fully validated ground truth for these fields.
