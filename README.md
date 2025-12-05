# NewsBot 2.0 — ITAI2373 Final Project

Professional News Intelligence Platform (course final project)

This repository is the scaffold and working codebase for the NewsBot Intelligence System 2.0, the final project for ITAI2373.

Contents
- A reproducible Python codebase for data processing, modeling, analysis, and a conversational interface (stubs and working baseline pipelines).
- Notebooks demonstrating data exploration and baseline classification.
- Tests and a CI workflow to validate core components.

High-level goals
- Ingest news articles and extract structured signals (categories, sentiment, topics, entities).
- Provide analysis modules for topic modeling, sentiment evolution, NER, and multilingual workflows.
- Offer a conversational retrieval interface and exportable reports for stakeholders.

Repository layout (top-level)

```
ITAI2373-NewsBot-Final/
├── README.md
├── requirements.txt
├── config/
├── src/                # source code (data processing, analysis, models, utils)
├── notebooks/          # exploration and training notebooks
├── tests/              # unit tests (pytest)
├── data/               # raw / processed / models / results
├── docs/               # technical documentation
└── reports/            # executive summary and final deliverables
```

Quick start (local)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

# NewsBot 2.0 — ITAI2373 Final Project

This repository contains the working code and supporting materials for the NewsBot Intelligence System 2.0.

If you're jumping in, here's the short version: the project ingests a large news dataset (created from your midterm notebook), extracts text features, and provides starter pipelines for classification, topic modeling, and exploratory analysis. The repository includes notebooks, small tests, and a baseline model you can run locally.

What you'll find here
- `src/` — modular Python code (data loaders, preprocessing, analysis, models, utilities).
- `notebooks/` — quick demos (data exploration and a baseline classification pipeline).
- `data/` — folders for storing raw data, processed datasets, trained models, and results.
- `tests/` — a few pytest tests covering the loader and baseline trainer.
- `docs/` — technical notes and implementation details.
- `reports/` — an executive summary and placeholders for final deliverables.

Quick start (local)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

2. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest joblib ijson
```

3. Quick data check:

- Open `notebooks/01_Data_Exploration.ipynb` to inspect `sample_newsbot_partial.json` and to produce `sample_for_modeling.csv` for quick experiments.

4. Run a baseline training demo (uses the sample CSV):

```powershell
python -m src.analysis.train_baseline --csv "c:\\Users\\javon\\Downloads\\NewsBot\\sample_for_modeling.csv" --model-out "data/models/baseline_pipeline.joblib"
```

Run tests

```powershell
pytest -q
```

Notes and assumptions
- The dataset was generated from your midterm notebook and lives locally as `newsbot_dataset_final.json` (about 200MB). For quick iteration I included `sample_newsbot_partial.json`.
- The code currently uses `processed_text_str` as the primary text field for modeling. If you later provide full article text, update the loader and notebooks to use it.
- API keys (for external LLMs or translation APIs) should be placed in `config/api_keys_template.txt` and never committed with real secrets.

Future work (short, practical list)

1) Full-data training & final metrics
- Goal: Train the baseline pipeline on the full JSON using the streaming loader and capture final evaluation metrics.
- Deliverables: trained model (`data/models/baseline_pipeline.joblib`), `reports/metrics.md` with plots and numbers.

2) Topic modeling & visualizations
- Goal: Run LDA/NMF on tokens and produce human-readable topic labels and visualizations.
- Deliverables: `notebooks/03_Topic_Modeling.ipynb`, visual topic reports for `reports/`.

3) NER + relationship graphs
- Goal: Extract named entities with a pretrained model and build a co-occurrence graph to show relationships.
- Deliverables: expanded `src/analysis/ner_extractor.py`, `notebooks/04_NER_and_Relations.ipynb`, and network plots.

4) Summaries & examples
- Goal: Demonstrate production-style summaries (preferably with full article bodies). If full bodies are unavailable, show limited demos using `short_description`.

5) Conversational demo & deployment
- Goal: Add a tiny FastAPI app that exposes analysis endpoints and a retrieval-backed demo for queries.

If you want, I can implement items 1 and 2 next (full-data training + topic modeling). Say which items to prioritize and I will continue implementing code, notebooks, and reports.
- Goal: Demonstrate abstractive summarization (for now using `short_description`; replace with full bodies if available) with a small transformer model or hosted API.

- Artifacts: `notebooks/05_Summarization.ipynb`, `src/language_models/summarizer.py` (enhanced), examples in `reports/`.
