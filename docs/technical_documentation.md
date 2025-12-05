## Technical documentation

This document explains the code organization, the dataset schema we've observed, and the practical pipelines to reproduce experiments. It focuses on actionable steps and clear next tasks.

### Project layout
- `src/data_processing`: data loaders, validators, preprocessors
- `src/analysis`: training scripts, classification & analysis helpers
- `src/language_models`: summarization and embedding wrappers
- `src/multilingual`: language detection and translation utilities
- `src/conversation`: query processing and response generation
- `src/utils`: plotting, evaluation and IO helpers

### Observed data schema
Use `processed_text_str` as the primary text column for modeling. Typical fields in each JSON record:
- `link` — original URL (use as id)
- `headline` — headline string
- `category` — target label for supervised tasks
- `short_description` — article excerpt
- `authors` — author string
- `date` — ISO-style date (YYYY-MM-DD)
- `processed_content` — token list (pre-tokenized)
- `processed_text_str` — normalized token string (preferred input)
- `sentiment` — numeric sentiment score (optional)

### Ingestion & preprocessing (recommended)
1. Stream the large JSON with `src.data_processing.loader.stream_json(path)` to avoid OOM (uses `ijson` if available).
2. Normalize text: lowercase, collapse whitespace, remove control characters.
3. Tokenize and clean with spaCy (or NLTK): remove stopwords, non-alphanumeric tokens, and optionally lemmatize.
4. Persist cleaned outputs to `data/processed/` (CSV or parquet) so experiments are repeatable.

Practical tip: create a small, representative sample (we include `sample_newsbot_partial.json`) to iterate quickly.

### Baseline classification
- Pipeline: TF-IDF (unigrams + bigrams, limit features) → LogisticRegression.
- Files: `notebooks/02_Baseline_Classification.ipynb`, `src/analysis/train_baseline.py`.
- Evaluation: use stratified splits and report accuracy plus precision/recall/F1 per class. Save the pipeline with `joblib` to `data/models/`.

### Topic modeling
- Options: LDA (gensim) or NMF (scikit-learn). Input can be token lists or TF-IDF matrix.
- Evaluate with coherence metrics and manually inspect top terms.

### NER and relation extraction
- Use pretrained spaCy models or transformer-based NER on `short_description` and `processed_text_str`.
- Aggregate entities and build co-occurrence graphs to identify common relations and central entities.

### Summarization & LM-based features
- Abstractive summarization needs full article bodies for best results. For demonstrations, use `headline + short_description` as input.
- For generation tasks, use a small transformer or a hosted LLM (store keys in `config/api_keys_template.txt`).

### Multilingual considerations
- Dataset appears English-only. To demo cross-lingual features add non-English sources or translate a subset with an API.

### Deployment suggestions
- Minimal demo: FastAPI with endpoints for analysis, query, and topics. Containerize with Docker for portability.

### Evaluation & reproducibility
- Pin dependencies in `requirements.txt`.
- Record random seeds and split hashes. Save processed data and trained models to `data/models/`.

### Known limitations and assumptions
- No full article bodies were present in the dataset, which limits summarization and deeper NER work.
- No labeled NER data exists — entity evaluation will be qualitative unless annotated.
- No explicit license metadata was found in the provided files. Confirm reuse permissions before making the dataset public.

### Immediate next steps
1. Implement a streaming trainer that partitions the dataset into `train/val/test` and writes compact CSVs.
2. Add notebooks for topic modeling and named-entity analysis (with example outputs for the report).
3. Optionally add a small FastAPI demo and Dockerfile for a runnable showcase.


