from __future__ import annotations
import json
from pathlib import Path

def read_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
