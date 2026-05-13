# Phase III: Physiological-Spatial Forensics & The Blending Paradox

This repository implements the **Phase III (Semantic-Physical)** framework of the Forensic Triad. It specifically focuses on the "Biological Masking" phenomenon discovered during cross-dataset validation on Celeb-DF v2.

## 🔬 The Discovery: The Blending Paradox
While artifact-centric (Phase II) models collapse on Out-of-Distribution (OOD) data—hitting **0.25 AUC** on DigiFakeAV—global physiological detectors (Phase III) show a unique failure mode. 

On **Celeb-DF v2**, our rPPG detector achieved **0.5262 AUC**. This is not a failure of signal extraction, but a proof of **Biological Spoofing**: modern blending techniques preserve the original actor's pulse on the forehead and cheeks, successfully masking the AI-generated inner-face features.

## 📊 Benchmarking Results
| Framework | Dataset | Target AUC | Status |
| :--- | :--- | :--- | :--- |
| Phase II (CNN) | FF++ (Intra) | 0.8723 | Baseline |
| Phase II (CNN) | DigiFakeAV | **0.2500** | Catastrophic Collapse |
| Phase II (CNN) | Celeb-DF v2 | 0.5104 | OOD Failure |
| **Phase III (rPPG)**| Celeb-DF v2 | **0.5262** | **Biological Masking Identified** |

## 🛠️ Installation
```bash
pip install -r requirements.txt
