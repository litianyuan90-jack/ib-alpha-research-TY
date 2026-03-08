from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AgentConfig:
    model: str = os.getenv("OPENAI_MODEL", "gpt-5")
    output_dir: Path = Path("outputs")
    reasoning_effort: str = "medium"
