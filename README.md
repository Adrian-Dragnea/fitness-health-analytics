# 🏋️ Fitness & Health Analytics (Work-in-progress)

End-to-end **ETL and Exploratory Data Analysis (EDA)** pipeline for fitness & health datasets, designed with **production-style structure**, **reproducibility**, and **cross-machine consistency** in mind.

---

## 🚀 Project Highlights

- Config-driven ETL pipeline (no hardcoded paths)
- Exploratory Data Analysis with Jupyter notebooks
- Centralized data storage on a NAS
- Linux execution via WSL for consistent behavior
- Clean separation between ETL and EDA

---

## 🗂️ Project Structure
```bash
fitness-health-analytics/
├── notebooks/                # Exploratory analysis (EDA only)
│   └── EDA.ipynb
│
├── src/                      # ETL pipeline source code
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── utils/
│
├── config/
│   └── .env           
│   └── local.yaml            # Centralized configuration
│
│
├── data/                    
│
│
├── logs/                     # Pipeline logs (NAS)
├── requirements.txt
└── .venv/                    # Virtual environment (ignored by git)
```

---

## ⚙️ Tech Stack

- **Python** (pandas, numpy)
- **Jupyter** (EDA)
- **YAML config** (pyyaml)
- **WSL 2 (Ubuntu)**
- **NAS storage**

---

## 🗄️ Data Architecture

Data is stored on a **Network Attached Storage (NAS)** and mounted into WSL:
```bash
/mnt/nas/Projects/fitness-health-analytics/
├── data/
│   ├── raw/
│   └── processed/
└── logs/
```

This mirrors real-world production setups by separating compute from storage.

---

## 🔁 Pipeline Overview

- **Extract**: Download datasets (e.g. Kaggle)
- **Transform**: Clean, validate, and prepare data
- **Load**: Store processed outputs back to NAS

EDA is performed separately in notebooks and informs ETL design decisions.

---

## ▶️ Run the Pipeline

```bash
source .venv/bin/activate
python run_pipeline.py
```

---

##🔒 Not Tracked in Git

Virtual environments

Raw datasets

Logs

Secrets (.venv)

---