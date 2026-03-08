from __future__ import annotations
from pathlib import Path
from datetime import datetime
from ib_alpha_agent.models import ResearchOutput

def render_report(output: ResearchOutput, output_dir: str | Path = "outputs") -> Path:
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe = "".join(c for c in output.company if c.isalnum() or c in ("-", "_")) or "company"
    path = out_dir / f"{safe}-{ts}.md"
    valuation_block = "\n".join(f"- **{item.method}**：{item.summary}" for item in output.valuation_notes) or "- 无"
    text = f"""# {output.company} {output.ticker or ''}

## Executive Summary
{output.executive_summary}

## Main Report
{output.body_markdown}

## Valuation Helper Notes
{valuation_block}

## Comparable Summary
{output.comparable_notes or '无'}
"""
    path.write_text(text, encoding="utf-8")
    return path
