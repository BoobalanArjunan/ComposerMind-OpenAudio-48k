---
license: cc-by-4.0
task_categories:
- text-to-audio
- audio-classification
- feature-extraction
language:
- en
tags:
- audio
- music
- sound
- game-audio
- electronic
- dsp
- pytorch
- benchmark
pretty_name: ComposerMind OpenAudio-48k
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: metadata.csv
---

# ComposerMind OpenAudio-48k: High-Fidelity Audio Dataset for Machine Learning Research

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-OpenAudio--48k-yellow.svg)](https://huggingface.co/datasets/boobalanit/ComposerMind-OpenAudio-48k)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-OpenAudio--48k-blue.svg)](https://www.kaggle.com/datasets/boobalanarjunan/composermind-openaudio-48k)
[![Audio Format](https://img.shields.io/badge/Audio-48kHz%2024--bit%20PCM%20Stereo-blue.svg)]()
[![Tracks](https://img.shields.io/badge/Tracks-94%20Unique%20Tracks-green.svg)]()
[![Total Duration](https://img.shields.io/badge/Duration-3.88%20Hours-orange.svg)]()
[![Publisher](https://img.shields.io/badge/Publisher-ComposerMind%20Labs-purple.svg)]()

## Overview
**ComposerMind OpenAudio-48k** is a research-oriented collection of **94 synthetically produced, high-energy electronic music tracks**, designed around fast-paced world exploration, interactive gaming, action sequences, and immersive electronic soundscapes.

Each track is accompanied by rich acoustic annotations generated using **BeatMind AI** (ComposerMind's proprietary acoustic analysis model and analysis pipeline), including tempo (BPM), musical key and Camelot harmonic notation, harmonic/percussive energy characteristics, and audio dynamics.

The dataset also provides a natural-language prompt for each track, intended to support text-to-audio generation, music captioning, semantic retrieval, and audio–text representation learning.

> **Acoustic Production Provenance:**  
> ComposerMind OpenAudio-48k is a **Studio-Grade, In-The-Box (ITB) Electronic Music Corpus**. Tracks are composed and digitally synthesized using professional studio sound generators, sequencers, and synthesizers inside a digital audio workstation (DAW). Every track was mastered and audited through **WaveWash DSP** to ensure zero digital overs ($0\text{ dBFS}$ clamping), balanced dynamic crest factor ($15.1\text{ dB}$ avg), and uniform 48kHz/24-bit headroom.

---

### Research Objectives
The dataset is designed to support:
* **Music Information Retrieval (MIR):** tempo estimation, key detection, harmonic analysis, rhythmic characterization, and audio feature extraction.
* **Generative Music AI:** prompt-conditioned generation experiments using compatible models and frameworks such as MusicGen, AudioCraft, and Stable Audio Open.
* **Audio–Text Representation Learning:** matching music recordings with natural-language descriptions for retrieval and embedding research.
* **Game Audio Research:** exploration of energetic electronic music suitable for interactive worlds, action environments, and gameplay experiences.
* **Dataset Quality and Benchmarking:** reproducible testing of audio analysis pipelines, metadata consistency, and acoustic feature estimation.

### Intended Users
The collection is intended for academic researchers, AI/ML engineers, music information retrieval specialists, game-audio developers, generative music researchers, sound designers, students, and music technology companies.

### Annotation Methodology
Acoustic annotations are produced using ComposerMind's proprietary **BeatMind AI** analysis workflow. The supplied annotations are **automatically extracted labels** and provide a standardized baseline for benchmark evaluation.

Natural-language prompts are provided as conditioning and descriptive metadata for Text-to-Audio generative models (such as MusicGen, AudioCraft, Stable Audio Open, and MusicLM).

---

## Technical Specifications
* **Dataset Name**: ComposerMind OpenAudio-48k
* **Creator & Author**: Boobalan Arjunan
* **Publisher**: ComposerMind Labs
* **Copyright**: Copyright © 2024 Boobalan Arjunan
* **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
* **Total Unique Tracks**: 94 tracks (`OpenAudio48k_Track01.wav` through `OpenAudio48k_Track94.wav`)
* **Total Audio Duration**: 3.88 hours (13,985.6 seconds / 233.1 minutes)
* **Dataset Disk Size**: 3.75 GB (uncompressed 24-bit linear PCM)
* **Sampling Rate**: 48,000 Hz (uniform across 100% of files)
* **Bit Depth**: 24-bit Linear PCM (`pcm_s24le`)
* **Channels**: 2 (Stereo)
* **Dynamic Range & Signal Integrity**:
  * Peak Level: Maximum -0.01 dBFS, Average -1.98 dBFS
  * Digital Overs / Clipping: 0 / 94 files (clean headroom preserved)
  * Average Dynamic Range (Crest Factor): 15.10 dB (Range: 11.33 dB – 17.90 dB)
  * Average RMS Energy: -17.09 dBFS (balanced commercial game-audio standard)
* **Tempo & Key Profile**:
  * BPM Range: 93.7 – 176.5 BPM (Average: 123.8 BPM)
  * Key Distribution: Diverse coverage across minor and major keys with exact Camelot codes (6A, 7A, 9A, 12B, etc.)
  * Timbre Breakdown: Average 80.1% Harmonic / 19.9% Percussive energy

---

## Dataset Structure
```
ComposerMind-OpenAudio-48k/
├── metadata.csv                 # Complete 94-track manifest (23 columns)
├── dataset-metadata.json        # Kaggle 10.0 Usability dataset specification
├── starter_eda_pytorch.ipynb    # Ingestion-ready PyTorch Dataset/DataLoader starter
├── LICENSE                      # Creative Commons Attribution 4.0 International
├── README.md                    # Official dataset card & benchmark guide
├── scripts/
│   └── audit_dataset.py         # Non-destructive WAV verification tool
└── docs/
    └── METADATA_REVIEW.md       # Audit history & verification log
```

### Metadata Schema (`metadata.csv` — 23 Columns)
The reviewed release manifest contains 23 high-relevance attributes:
1. `file_name`: Standardized audio filename (`OpenAudio48k_TrackXX.wav`)
2. `track_id`: Unique track identifier (`Track01` - `Track94`)
3. `title`: Track title (`ComposerMind OpenAudio-48k - Track XX`)
4. `artist`: Creator / Author (**Boobalan Arjunan**)
5. `publisher`: Publishing entity (**ComposerMind Labs**)
6. `copyright`: `Copyright © 2024 Boobalan Arjunan`
7. `license`: `CC-BY-4.0`
8. `primary_genre`: `Electronic`
9. `sub_genre`: `Game Audio / Drum & Bass / Breakbeat`
10. `mood_label`: `Energetic / Dynamic Exploration`
11. `tempo_bpm`: Continuous tempo detected via BeatMind AI
12. `musical_key`: Detected musical key (e.g. `G Minor`, `E Minor`)
13. `camelot_code`: Camelot Wheel harmonic mixing code (`6A`, `9A`, etc.)
14. `harmonic_ratio`: Percentage of harmonic/tonal energy (0–100%)
15. `percussive_ratio`: Percentage of transient/percussive energy (0–100%)
16. `crest_factor_db`: Dynamic range (peak-to-RMS ratio in dB)
17. `duration_seconds`: Precise duration in seconds
18. `sample_rate`: Sampling frequency (48,000 Hz)
19. `channels`: Channel layout (2 = Stereo)
20. `bit_depth`: Audio resolution (24 bits)
21. `peak_dbfs`: Maximum absolute peak level in dBFS
22. `rms_dbfs`: Root-mean-square energy level in dBFS
23. `text_prompt`: Turnkey natural language training caption for Text-to-Music models

*(Note: `record_label`, `musical_scale`, `bpm_confidence`, and `groove_quantization` were streamlined to remove redundancy and ensure maximum interpretability for research).*

---

## Python Ingestion Example

### Training / Ingestion with PyTorch & Pandas
```python
import os
import pandas as pd
import torchaudio

dataset_dir = "/path/to/ComposerMind_OpenAudio_48k"
df = pd.read_csv(os.path.join(dataset_dir, "metadata.csv"))

# Inspect ground-truth labels
print(df[["file_name", "tempo_bpm", "musical_key", "camelot_code", "text_prompt"]].head(3))

# Load audio waveform
sample_row = df.iloc[0]
audio_path = os.path.join(dataset_dir, sample_row["file_name"])
waveform, sample_rate = torchaudio.load(audio_path)

print(f"Loaded: {sample_row['title']}")
print(f"Tensor Shape: {waveform.shape}, Sample Rate: {sample_rate} Hz")
print(f"Text Prompt: {sample_row['text_prompt']}")
```

---

## Audio Download & Public Registries

The uncompressed 3.75 GB 24-bit audio tracks are hosted on public open-access data registries:

* **Hugging Face Hub:** [huggingface.co/datasets/boobalanit/ComposerMind-OpenAudio-48k](https://huggingface.co/datasets/boobalanit/ComposerMind-OpenAudio-48k)
* **Kaggle Dataset:** [kaggle.com/datasets/boobalanarjunan/composermind-openaudio-48k](https://www.kaggle.com/datasets/boobalanarjunan/composermind-openaudio-48k)
* **Zenodo DOI:** *Pending minting upon final deposit*

---

## Attribution & Citation
Published under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

### BibTeX
```bibtex
@dataset{arjunan2024composermindopenaudio,
  title     = {ComposerMind OpenAudio-48k: A High-Fidelity Audio Dataset for Machine Learning Research},
  author    = {Arjunan, Boobalan},
  publisher = {ComposerMind Labs},
  year      = {2024},
  license   = {Creative Commons Attribution 4.0 International (CC BY 4.0)}
}
```
