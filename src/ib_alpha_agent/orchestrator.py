from __future__ import annotations
from ib_alpha_agent.config import AgentConfig
from ib_alpha_agent.models import FactsPack, PeerItem, ResearchOutput
from ib_alpha_agent.prompts import SYSTEM_PROMPT, build_user_prompt
from ib_alpha_agent.llm import run_llm
from ib_alpha_agent.valuation import build_valuation_skeleton
from ib_alpha_agent.comparables import summarize_peers

def run_research(facts: FactsPack, peers: list[PeerItem], cfg: AgentConfig) -> ResearchOutput:
    prompt = build_user_prompt(facts, peers)
    body = run_llm(
        instructions=SYSTEM_PROMPT,
        prompt=prompt,
        model=cfg.model,
        reasoning_effort=cfg.reasoning_effort,
    )
    return ResearchOutput(
        company=facts.company,
        ticker=facts.ticker,
        executive_summary=f"{facts.company} 的研究已完成。以下为基于事实包与同业对比生成的机构级初稿。",
        body_markdown=body,
        valuation_notes=build_valuation_skeleton(facts),
        comparable_notes=summarize_peers(peers),
    )
