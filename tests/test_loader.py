from src.data_processing.loader import stream_json
import os


def test_stream_json_sample_exists():
    sample = r"c:\Users\javon\Downloads\NewsBot\sample_newsbot_partial.json"
    assert os.path.exists(sample), f"Sample file not found: {sample}"
    # ensure generator yields at least one record
    gen = stream_json(sample)
    first = next(gen)
    assert isinstance(first, dict)

