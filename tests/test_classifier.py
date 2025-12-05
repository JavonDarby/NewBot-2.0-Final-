from src.analysis.train_baseline import train_baseline
import os


def test_train_baseline_runs():
    csv_path = r"c:\Users\javon\Downloads\NewsBot\sample_for_modeling.csv"
    assert os.path.exists(csv_path), f"CSV not found: {csv_path}"
    model_out = r"c:\Users\javon\Downloads\NewsBot\ITAI2373-NewsBot-Final\data\models\temp_pipeline.joblib"
    pipeline, _ = train_baseline(csv_path, model_out)
    # predict on a couple of samples
    import pandas as pd
    df = pd.read_csv(csv_path)
    X = df['processed_text_str'].fillna('').iloc[:5]
    preds = pipeline.predict(X)
    assert len(preds) == 5
