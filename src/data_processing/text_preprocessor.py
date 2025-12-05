"""Text preprocessing utilities: tokenization, stopword removal, normalization."""

def preprocess_text(text: str) -> str:
    """Minimal placeholder function. Replace with robust pipeline."""
    if not text:
        return ""
    # simple lower-case/strip for now
    return text.lower().strip()
