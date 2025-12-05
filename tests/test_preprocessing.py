from src.data_processing.text_preprocessor import preprocess_text


def test_preprocess_empty():
    assert preprocess_text("") == ""


def test_preprocess_lower():
    assert preprocess_text("Hello") == "hello"
