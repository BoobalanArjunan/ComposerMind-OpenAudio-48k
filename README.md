# ComposerMind OpenAudio-48k

**Pre-release research dataset — metadata review completed; WAV validation and rights review pending**

ComposerMind OpenAudio-48k is a collection of **94 reported synthetically produced electronic music tracks** oriented toward **fast-paced world exploration, interactive gaming, action sequences, and electronic game soundtracks**. The collection combines full-mix recordings with track-level descriptive and audio-analysis metadata. It is intended to provide accessible material for reproducible experiments in music information retrieval (MIR), game-audio research, audio machine learning, and metadata quality assurance.

**Created by:** Boobalan Arjunan  
**Published by:** ComposerMind Labs  
**Reported original copyright:** © 2024 Boobalan Arjunan (rights to be confirmed)  
**Dataset release:** Not yet published or licensed

“Synthetically produced” describes electronically created music; it **does not establish** that a generative AI model created the music. Specific instruments, DAW processes and source material have not yet been audited.

## Why this dataset exists

Electronic music for games often combines strong rhythmic patterns, synthesized timbres, bass-heavy production and evolving atmospheric textures. Such music can be useful for testing algorithms that characterize tempo, tonal content, energy, timbre and overall musical structure. This collection aims to provide a consistent set of music recordings and machine-readable track metadata for exploration, education and baseline evaluation.

The metadata is a starting point for experiments, **not a verified ground-truth benchmark**. Reported genre, mood, tempo, key, Camelot and audio-feature annotations must be evaluated before they are used as authoritative labels.

## Who can use it?

- **MIR and audio ML researchers:** explore tempo, key, timbre, embedding extraction, similarity and music tagging.
- **Game-audio researchers and developers:** study characteristics of energetic electronic exploration music and prototype music-search workflows.
- **Dataset curators and ML engineers:** test audio/metadata validation, reproducibility, schema checks and data quality workflows.
- **Students and educators:** practice audio feature extraction, data loading, exploratory analysis and benchmark design.
- **Music technology developers:** prototype track discovery, classification and metadata enrichment pipelines.

Public download and reuse will depend on the final license and verified rights.

## Collection overview

| Property | Current metadata claim |
| --- | --- |
| Tracks | 94 |
| Style | Electronic; game audio / breakbeat / drum-and-bass influenced |
| Intended context | Fast-paced world exploration and gaming |
| Sample rate | 48,000 Hz |
| Channels | 2 (stereo) |
| Bit depth | 16-bit |
| Duration | Varies by track |
| Format | WAV |
| Annotations | Track identity, descriptive tags, tempo/key and audio features |

**Important:** The values above come from the supplied CSV, not direct verification of the WAVs.

## Possible research tasks

1. **Music information retrieval:** compare automated tempo and key estimators with supplied annotations after independent review.
2. **Audio embeddings and retrieval:** index tracks using learned representations and explore similarity and nearest-neighbor retrieval.
3. **Game-music tagging:** investigate descriptors for high-energy electronic exploration music; new independently labeled classes are needed for supervised multi-genre evaluation.
4. **Audio quality analytics:** inspect peak/RMS measurements and compare metadata with independently calculated audio statistics.
5. **Dataset engineering:** test metadata schema consistency, filename reconciliation, duplicate detection and release reproducibility.

Because all tracks currently share the same broad genre and mood tags, this dataset alone is **not** suitable as a multi-class genre or mood classification benchmark without additional labeled data.

## Metadata

The original user-supplied CSV contains 94 rows and 27 columns. A proposed 23-column reviewed CSV removes four redundant or insufficiently documented fields; see [metadata review](docs/METADATA_REVIEW.md). The descriptive field `text_prompt` was renamed to `track_description` to avoid implying a proven generation prompt. The license field is marked pending review until release rights are confirmed.

The original CSV is preserved separately by the dataset owner. Do not overwrite it without comparing the reviewed version.

## Validation and publication

Use the read-only local audio audit:

```bash
python3 scripts/audit_dataset.py "/Users/mymac/Desktop/Dataset Contanier/ComposerMind_OpenAudio_48k" --hash
```

The audit checks WAV inventory and technical properties and creates reports. It does not modify source recordings. Review [validation plan](validation/VALIDATION_PLAN.md) before publication.

**Release status:** The dataset audio is not hosted here; there is no public reuse license yet. After WAV/metadata/rights validation, release the final dataset card, immutable manifest, version and download links.
