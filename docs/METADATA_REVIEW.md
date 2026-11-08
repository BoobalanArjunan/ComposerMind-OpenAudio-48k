# ComposerMind OpenAudio-48k: Metadata & Audio Integrity Verification Log

**Verification Date:** November 8, 2026  
**Corpus:** ComposerMind OpenAudio-48k (94 Unique Tracks, 3.88 Audio Hours)  
**Author & Publisher:** Boobalan Arjunan / ComposerMind Labs  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  

---

## 1. Physical Audio Integrity Audit Results

An independent, non-destructive automated audit (`scripts/audit_dataset.py`) was executed across the full dataset container:

* **File Count:** Exactly **94 WAV audio tracks** found (0 missing, 0 duplicates).
* **Filename Reconciliation:** 100% of physical files reconciled 1:1 with `metadata.csv` (`OpenAudio48k_Track01.wav` through `OpenAudio48k_Track94.wav`).
* **Sampling Rate:** Uniform **48,000 Hz** across 100% of files.
* **Channels:** Uniform **Stereo (2 Channels)** across 100% of files.
* **Bit Depth / Format:** **24-bit Linear PCM (`PCM_24` / `pcm_s24le`)**.
* **Audio Duration:** 13,985.6 seconds (3.88 hours).
* **Dataset Disk Size:** 3.75 GB uncompressed linear PCM.
* **Decode & Header Status:** 100% of files decoded with status `OK` (0 header corruptions, 0 truncated payloads).

---

## 2. Dynamic Range & Headroom (WaveWash DSP Verification)

* **Peak Amplitudes:** Maximum $-0.01\text{ dBFS}$, Average $-1.98\text{ dBFS}$.
* **Digital Overs / Clipping:** **0 / 94 files** (no $0\text{ dBFS}$ flat-topping or saturation).
* **Dynamic Range (Crest Factor):** Average $15.10\text{ dB}$ (Range: $11.33\text{ dB} - 17.90\text{ dB}$).
* **RMS Energy:** Average $-17.09\text{ dBFS}$ (calibrated for commercial game-audio and generative modeling).

---

## 3. Metadata Manifest Schema (`metadata.csv`)

The finalized release manifest retains all 27 extracted features:
1. `file_name`: Exact relative filename matching local disk.
2. `track_id`: Unique track identifier (`Track01` to `Track94`).
3. `title`: Official track title.
4. `artist`: Boobalan Arjunan.
5. `record_label`: ComposerMind Labs.
6. `publisher`: ComposerMind Labs.
7. `copyright`: Copyright © 2024 Boobalan Arjunan.
8. `license`: CC-BY-4.0.
9. `primary_genre`: Electronic.
10. `sub_genre`: Game Audio / Drum & Bass / Breakbeat.
11. `mood_label`: Energetic / Dynamic Exploration.
12. `tempo_bpm`: Continuous tempo detected via BeatMind AI.
13. `bpm_confidence`: Tempo detection confidence score.
14. `musical_key`: Detected musical key (e.g., G Minor, E Minor).
15. `musical_scale`: Scale classification (Minor/Major).
16. `camelot_code`: Harmonic mixing key code (e.g., 6A, 9A, 12B).
17. `harmonic_ratio`: Harmonic/tonal energy percentage (HPSS).
18. `percussive_ratio`: Transient/percussive energy percentage (HPSS).
19. `crest_factor_db`: Peak-to-RMS dynamic range ratio in dB.
20. `groove_quantization`: Beat grid adherence metric.
21. `duration_seconds`: Track duration in seconds.
22. `sample_rate`: 48000 Hz.
23. `channels`: 2.
24. `bit_depth`: 24 bits.
25. `peak_dbfs`: Maximum absolute peak level.
26. `rms_dbfs`: Root-mean-square energy level.
27. `text_prompt`: Turnkey natural language training caption.

---

## 4. Release Checklist Status

- [x] All 94 WAV files verified and renamed to standard schema.
- [x] Bit depth confirmed as 24-bit PCM across all files and manifests.
- [x] `.DS_Store` and internal planning docs removed from public release container.
- [x] PyTorch DataLoader and EDA starter notebook tested and verified.
- [x] Kaggle dataset configuration (`dataset-metadata.json`) validated.
- [x] Git repository synced with verified release manifests, licenses, and docs.
