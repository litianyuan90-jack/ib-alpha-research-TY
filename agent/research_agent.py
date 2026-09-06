from __future__ import annotations

"""Backward-compatible entry point for the v3 package.

The research methodology is loaded by the core package from repository-level
SKILL.md. This wrapper intentionally contains no independent prompt or skill rules.
"""

import argparse
from ib_alpha_agent.config import AgentConfig
from ib_alpha_agent.models import FactsPack
from ib_alpha_agent.orchestrator import run_research
from ib_alpha_agent.reporting import render_report


def main():
    parser = argparse.ArgumentParser(description="IB Alpha compatibility research entry point")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--ticker", default=None, help="Ticker, e.g. 300442.SZ")
    parser.add_argument("--model", default="gpt-5", help="OpenAI model name")
    parser.add_argument("--output-dir", default="outputs", help="Output directory")
    parser.add_argument("--no-web-search", action="store_true", help="Disable read-only public web research")
    args = parser.parse_args()

    cfg = AgentConfig(
        model=args.model,
        output_dir=args.output_dir,
        enable_web_search=not args.no_web_search,
    )
    facts = FactsPack(company=args.company, ticker=args.ticker)
    result = run_research(facts, [], cfg)
    path = render_report(result, cfg.output_dir)

    print(f"Research status: {result.status}")
    print(f"Research report saved to: {path}")


if __name__ == "__main__":
    main()
