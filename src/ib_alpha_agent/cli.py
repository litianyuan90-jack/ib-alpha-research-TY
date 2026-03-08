from __future__ import annotations
import argparse
from ib_alpha_agent.config import AgentConfig
from ib_alpha_agent.sources import load_facts_pack, load_peers_pack
from ib_alpha_agent.orchestrator import run_research
from ib_alpha_agent.reporting import render_report

def main():
    parser = argparse.ArgumentParser(description="IB Alpha Agent v3")
    sub = parser.add_subparsers(dest="command", required=True)
    research = sub.add_parser("research", help="Run a research job")
    research.add_argument("--company", required=False, help="Company name override")
    research.add_argument("--ticker", required=False, help="Ticker override")
    research.add_argument("--facts-file", required=True, help="Path to JSON facts pack")
    research.add_argument("--peers-file", required=False, help="Path to peers JSON")
    research.add_argument("--model", default="gpt-5", help="OpenAI model")
    research.add_argument("--output-dir", default="outputs", help="Output directory")
    args = parser.parse_args()

    cfg = AgentConfig(model=args.model)
    cfg.output_dir = args.output_dir

    facts = load_facts_pack(args.facts_file)
    if args.company:
        facts.company = args.company
    if args.ticker:
        facts.ticker = args.ticker

    peers = load_peers_pack(args.peers_file)
    result = run_research(facts, peers, cfg)
    path = render_report(result, cfg.output_dir)
    print(f"Saved report to: {path}")

if __name__ == "__main__":
    main()
