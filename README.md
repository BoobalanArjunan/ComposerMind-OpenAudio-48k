# ComposerMind OpenAudio-48k: High-Fidelity Audio Dataset for Machine Learning Research

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Audio Format](https://img.shields.io/badge/Audio-48kHz%2024--bit%20PCM%20Stereo-blue.svg)]()
[![Tracks](https://img.shields.io/badge/Tracks-94%20Unique%20Tracks-green.svg)]()
[![Total Duration](https://img.shields.io/badge/Duration-3.88%20Hours-orange.svg)]()
[![Publisher](https://img.shields.io/badge/Publisher-ComposerMind%20Labs-purple.svg)]()

## Overview
**ComposerMind OpenAudio-48k** is an open-access, studio-grade audio benchmark corpus created and curated by **Boobalan Arjunan** and published by **ComposerMind Labs**. The dataset comprises **94 strictly unique, uncompressed studio-rendered WAV tracks** spanning high-energy electronic music, drum & bass breaks, and dynamic game exploration cues.

Engineered specifically as an all-purpose training and evaluation benchmark for machine learning, deep learning, and audio AI researchers, every track delivers pristine **48,000 Hz, 24-bit linear PCM stereo audio (`pcm_s24le`)** with **zero digital clipping**.

Every track is accompanied by rich acoustic ground-truth labels extracted via **BeatMind AI / TempoMind** (BPM, musical scale/key, Camelot code, harmonic/percussive ratio, dynamic range) and a **turnkey natural language prompt** for immediate use in Text-to-Audio generative models (such as MusicGen, AudioCraft, Stable Audio Open, and MusicLM).

> **Acoustic Production Provenance:**  
> ComposerMind OpenAudio-48k is a **Studio-Grade, In-The-Box (ITB) Electronic Music Corpus**. Tracks are composed and digitally synthesized using professional studio sound generators, sequencers, and synthesizers inside a digital audio workstation (DAW). Every track was mastered and audited through **WaveWash DSP** to ensure zero digital overs ($0\text{ dBFS}$ clamping), balanced dynamic crest factor ($15.1\text{ dB}$ avg), and uniform 48kHz/24-bit headroom.

---

## Technical Specifications
* **Dataset Name**: ComposerMind OpenAudio-48k
* **Creator & Author**: Boobalan Arjunan
* **Record Label & Publisher**: ComposerMind Labs
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
* **Tempo & Scale Profile**:
  * BPM Range: 93.7 – 176.5 BPM (Average: 123.8 BPM)
  * Key Distribution: Diverse coverage across minor and major keys (E Minor, D Minor, E Major, C Minor, D Major, G Minor, etc.) with exact Camelot codes (6A, 7A, 9A, 12B, etc.)
  * Timbre Breakdown: Average 80.1% Harmonic / 19.9% Percussive energy

---

## Machine Learning Ground-Truth Labels & Applications
Every track in `metadata.csv` provides multi-dimensional ground truth labels for 5 major machine learning training paradigms:

| Machine Learning Task | Ground-Truth Column | Model Architecture Examples |
| :--- | :--- | :--- |
| **1. Text-to-Audio / Music Generation** | `text_prompt`, `tempo_bpm`, `musical_key` | MusicGen, AudioCraft, Stable Audio Open, MusicLM |
| **2. Tempo & Beat Tracking Estimation** | `tempo_bpm`, `bpm_confidence` | BeatNet, TempoCNN, DeepRhythm |
| **3. Musical Key & Scale Classification** | `musical_key`, `musical_scale`, `camelot_code` | 24-class KeyNet, MIR key estimation networks |
| **4. Timbre & Texture Conditioning** | `harmonic_ratio`, `percussive_ratio` | Conditional diffusion models (controlling synth vs drum density) |
| **5. Multi-Label Tagging & Contrastive Learning** | `primary_genre`, `sub_genre`, `mood_label` | CLAP (Audio-Language contrastive learning), AST, MusiCNN |

---

## Sample Text Prompts for Generative AI (Text-to-Music)
In `metadata.csv`, each audio track has a pre-formatted, detailed natural language training prompt:

* **Track 01**:
  > *"A high-energy, dynamic electronic game exploration soundtrack track at 157.9 BPM in G Minor (6A). Features driving rolling breakbeats, deep sub-bassline, atmospheric ambient synths, 60.2% harmonic textures, and crisp percussive transients suitable for interactive game audio."*
* **Track 46**:
  > *"A high-energy, dynamic electronic game exploration soundtrack track at 150.0 BPM in E Minor (9A). Features driving rolling breakbeats, deep sub-bassline, atmospheric ambient synths, 84.6% harmonic textures, and crisp percussive transients suitable for interactive game audio."*
* **Track 94**:
  > *"A high-energy, dynamic electronic game exploration soundtrack track at 115.4 BPM in D Minor (7A). Features driving rolling breakbeats, deep sub-bassline, atmospheric ambient synths, 82.5% harmonic textures, and crisp percussive transients suitable for interactive game audio."*

---

## Repository & Dataset Structure
```
ComposerMind-OpenAudio-48k/
├── metadata.csv                 # Complete 94-track manifest (27 columns)
├── dataset-metadata.json        # Kaggle 10.0 Usability dataset specification
├── starter_eda_pytorch.ipynb    # Ingestion-ready PyTorch Dataset/DataLoader starter
├── LICENSE                      # Creative Commons Attribution 4.0 International
├── README.md                    # Official dataset card & benchmark guide
├── scripts/
│   └── audit_dataset.py         # Non-destructive WAV verification tool
└── docs/
    └── METADATA_REVIEW.md       # Audit history & verification log
```

### Metadata Schema (`metadata.csv`)
27 columns included in the CSV manifest:
* `file_name`: Standardized filename (`OpenAudio48k_TrackXX.wav`)
* `track_id`: Unique track identifier (`Track01` - `Track94`)
* `title`: Track title (`ComposerMind OpenAudio-48k - Track XX`)
* `artist`: Creator / Author (**Boobalan Arjunan**)
* `record_label`: Releasing label (**ComposerMind Labs**)
* `publisher`: Publishing entity (**ComposerMind Labs**)
* `copyright`: `Copyright © 2024 Boobalan Arjunan`
* `license`: `CC-BY-4.0`
* `primary_genre`: `Electronic`
* `sub_genre`: `Game Audio / Drum & Bass / Breakbeat`
* `mood_label`: `Energetic / Dynamic Exploration`
* `tempo_bpm`: Continuous float BPM detected via BeatMind AI
* `bpm_confidence`: Neural tempo detection confidence percentage
* `musical_key`: Detected musical key (e.g. `G Minor`, `E Minor`)
* `musical_scale`: Scale mode (`Minor` / `Major`)
* `camelot_code`: Camelot Wheel harmonic mixing code (`6A`, `9A`, etc.)
* `harmonic_ratio`: Percentage of harmonic/tonal energy (0–100%)
* `percussive_ratio`: Percentage of transient/percussive energy (0–100%)
* `crest_factor_db`: Dynamic range (peak-to-RMS ratio in dB)
* `groove_quantization`: Beat grid adherence score
* `duration_seconds`: Precise duration in seconds
* `sample_rate`: Sampling frequency (48,000 Hz)
* `channels`: Channel layout (2 = Stereo)
* `bit_depth`: Audio resolution (24 bits)
* `peak_dbfs`: Maximum absolute peak level in dBFS
* `rms_dbfs`: Root-mean-square energy level in dBFS
* `text_prompt`: Turnkey natural language training caption for Text-to-Music models

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

## Audio Download & Mirrors

The uncompressed 3.75 GB 24-bit audio tracks are hosted on public open-access data registries:

* **Kaggle Dataset:** [kaggle.com/datasets/boobalanarjunan/composermind-openaudio-48k](https://www.kaggle.com/datasets/boobalanarjunan/composermind-openaudio-48k)
* **Hugging Face Hub:** [huggingface.co/datasets/ComposerMind/OpenAudio-48k](https://huggingface.co/datasets/ComposerMind/OpenAudio-48k)
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
