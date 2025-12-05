"""Train a baseline classifier (TF-IDF + LogisticRegression).

Usage (python -m src.analysis.train_baseline):
- Reads a CSV with columns: `processed_text_str` and `category` (or headline)
- Splits data, trains TF-IDF + LogisticRegression, prints metrics, and saves model & vectorizer
"""

import os
import joblib
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd


def train_baseline(csv_path: str, model_out: str = None):
    df = pd.read_csv(csv_path)
    if 'processed_text_str' in df.columns:
        X = df['processed_text_str'].fillna('')
    elif 'short_description' in df.columns:
        X = df['short_description'].fillna('')
    else:
        raise ValueError('CSV must contain processed_text_str or short_description')

    if 'category' not in df.columns:
        raise ValueError('CSV must contain a `category` column for supervised classification')
    y = df['category'].fillna('')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=20000, ngram_range=(1,2))),
        ('clf', LogisticRegression(max_iter=1000, solver='liblinear'))
    ])

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    report = metrics.classification_report(y_test, preds, zero_division=0)
    accuracy = metrics.accuracy_score(y_test, preds)

    print('Accuracy:', accuracy)
    print(report)

    if model_out:
        os.makedirs(os.path.dirname(model_out), exist_ok=True)
        joblib.dump(pipeline, model_out)
        print('Saved model to', model_out)

    return pipeline, (X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, required=True, help='Input CSV for training (sample_for_modeling.csv)')
    parser.add_argument('--model-out', type=str, default='data/models/baseline_pipeline.joblib')
    args = parser.parse_args()

    train_baseline(args.csv, args.model_out)
