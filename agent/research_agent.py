from __future__ import annotations

import argparse
import os
from pathlib import Path
from datetime import datetime
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skill" / "IB_ALPHA_SKILL_V2.md"
PROMPT_PATH = ROOT / "templates" / "prompt-template.md"
OUTPUT_DIR = ROOT / "agent" / "outputs"

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def build_prompt(company: str, ticker: str | None) -> str:
    template = load_text(PROMPT_PATH)
    target = company if not ticker else f"{company} {ticker}"
    return template.replace("【公司名 / 股票代码】", target)

def run_research(company: str, ticker: str | None, model: str = "gpt-5") -> Path:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    system_prompt = load_text(SKILL_PATH)
    user_prompt = build_prompt(company, ticker)

    response = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    text = getattr(response, "output_text", None) or str(response)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_name = "".join(c for c in company if c.isalnum() or c in ("-", "_")) or "company"
    out = OUTPUT_DIR / f"{safe_name}-{ts}.md"
    out.write_text(text, encoding="utf-8")
    return out

def main():
    parser = argparse.ArgumentParser(description="Run IB Alpha equity research agent")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--ticker", default=None, help="Ticker, e.g. 300442.SZ")
    parser.add_argument("--model", default="gpt-5", help="OpenAI model name")
    args = parser.parse_args()

    if "OPENAI_API_KEY" not in os.environ:
        raise RuntimeError("Please set OPENAI_API_KEY first.")

    out = run_research(args.company, args.ticker, args.model)
    print(f"Research report saved to: {out}")

if __name__ == "__main__":
    main()
