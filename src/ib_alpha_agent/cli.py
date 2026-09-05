from __future__ import annotations
import argparse
from ib_alpha_agent.config import AgentConfig
from ib_alpha_agent.models import FactsPack
from ib_alpha_agent.sources import load_facts_pack, load_peers_pack
from ib_alpha_agent.orchestrator import run_research
from ib_alpha_agent.reporting import render_report


def main():
    parser = argparse.ArgumentParser(description="IB Alpha Agent v3")
    sub = parser.add_subparsers(dest="command", required=True)
    research = sub.add_parser("research", help="Run a research job")
    research.add_argument("--company", required=False, help="Company name override or target when no facts file is supplied")
    research.add_argument("--ticker", required=False, help="Ticker override, e.g. 300442.SZ")
    research.add_argument("--facts-file", required=False, help="Optional JSON facts pack; the agent can research publicly when omitted")
    research.add_argument("--peers-file", required=False, help="Optional peers JSON")
    research.add_argument("--model", default="gpt-5", help="OpenAI model")
    research.add_argument("--output-dir", default="outputs", help="Output directory")
    research.add_argument(
        "--no-web-search",
        action="store_true",
        help="Disable read-only public web research and rely on supplied facts / model knowledge only",
    )
    args = parser.parse_args()

    cfg = AgentConfig(model=args.model)
    cfg.output_dir = args.output_dir
    cfg.enable_web_search = not args.no_web_search

    if args.facts_file:
        facts = load_facts_pack(args.facts_file)
    else:
        if not args.company:
            research.error("--company is required when --facts-file is omitted")
        facts = FactsPack(company=args.company, ticker=args.ticker)

    if args.company:
        facts.company = args.company
    if args.ticker:
        facts.ticker = args.ticker

    peers = load_peers_pack(args.peers_file)
    result = run_research(facts, peers, cfg)
    path = render_report(result, cfg.output_dir)
    print(f"Research status: {result.status}")
    print(f"Saved report to: {path}")


if __name__ == "__main__":
    main()
