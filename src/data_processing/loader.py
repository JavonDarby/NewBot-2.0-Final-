"""Streaming loader for large JSON arrays.

Attempts to use ijson for streaming; if ijson is unavailable, falls back to loading the whole file
(with a warning). The dataset from the midterm is a single large JSON array of article objects.
"""

from typing import Iterator, Dict
import json
import logging

try:
    import ijson  # type: ignore
    HAS_IJSON = True
except Exception:
    HAS_IJSON = False


def stream_json(path: str) -> Iterator[Dict]:
    """Yield records from a JSON array file.

    If `ijson` is available, uses it to avoid loading the entire file into memory.
    Otherwise, falls back to json.load (OK for moderate sizes).
    """
    if HAS_IJSON:
        logging.info('Using ijson for streaming JSON: %s', path)
        with open(path, 'rb') as f:
            # ijson.items with prefix 'item' iterates array elements
            for obj in ijson.items(f, 'item'):
                yield obj
    else:
        logging.warning('ijson not installed: falling back to json.load (may use a lot of memory)')
        with open(path, 'r', encoding='utf8') as f:
            data = json.load(f)
            for obj in data:
                yield obj
