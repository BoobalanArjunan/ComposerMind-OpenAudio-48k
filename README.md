# ComposerMind OpenAudio-48k

**Pre-release | Validation pending**

ComposerMind OpenAudio-48k is a collection of **94 reported synthetically created electronic music tracks**, focused on **fast-paced world-exploration and gaming-oriented electronic genres**. The recordings are intended for audio machine learning, music information retrieval, and game-audio research.

**Synthetic production** here refers to electronically produced music, such as synthesized instruments and programmed arrangements. It does **not** imply generative-AI production; the exact production methods will be documented after verification.

## Attribution

- **Created by:** Boobalan Arjunan
- **Published by:** ComposerMind Labs
- **Collection:** 94 tracks (reported; pending file audit)
- **Target format:** 48 kHz WAV (pending verification)
- **Metadata:** CSV and JSON metadata (pending schema and value audit)
- **License:** Not yet finalized. No redistribution permission is granted by this repository until a license is published.

## Intended research applications

- Electronic and game-music genre tagging
- Tempo, key, energy and structural analysis
- Music information retrieval and audio representation learning
- Metadata validation and audio quality benchmarking

These are proposed uses, not benchmark results.

## Validation

Run the non-destructive audit on your local dataset folder:

```bash
python3 scripts/audit_dataset.py "/Users/mymac/Desktop/Dataset Contanier/ComposerMind_OpenAudio_48k"
```

The audit writes reports to a separate output directory by default and **never renames, edits, resamples, or deletes source audio**. Review `validation/VALIDATION_PLAN.md` before release.

## Publication plan

1. Reconcile the actual WAV inventory against metadata CSV/JSON.
2. Verify file encoding, sample rates, channels, durations, duplicates and annotation consistency.
3. Review composition, recording, performance and sample rights.
4. Document generation/production methods, limitations and intended tasks.
5. Publish a versioned dataset card and validated audio on an appropriate dataset platform.

**Status:** This repository is documentation and tooling only. The 94 tracks are not yet validated or released here.
