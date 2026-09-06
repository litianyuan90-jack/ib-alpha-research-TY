from __future__ import annotations
from ib_alpha_agent.config import AgentConfig
from ib_alpha_agent.models import FactsPack, PeerItem, ResearchOutput, ResearchStatus
from ib_alpha_agent.prompts import SYSTEM_PROMPT, build_user_prompt
from ib_alpha_agent.llm import run_llm
from ib_alpha_agent.valuation import build_valuation_skeleton
from ib_alpha_agent.comparables import summarize_peers


QUALITY_MARKERS: dict[str, tuple[str, ...]] = {
    "research_cutoff": ("Research Cutoff", "研究截止", "数据截止"),
    "industry": ("Industry", "行业"),
    "business_model": ("Business Model", "商业模式"),
    "financial_quality": ("Financial Quality", "财务质量"),
    "valuation": ("Valuation", "估值"),
    "catalysts": ("Catalysts", "催化剂"),
    "risks": ("Risks", "风险"),
    "governance": ("Governance", "治理"),
    "final_view": ("Final View", "最终观点", "投资结论"),
    "thesis_break": ("What Would Change My Mind", "改变我的判断", "thesis-break", "论点失效"),
    "five_metrics": ("Five Metrics", "5个", "五个", "持续跟踪"),
    "unknowns": ("Unknowns", "Follow-up Diligence", "待核实", "未知项", "补充尽调"),
    "fact_inference_judgment": ("Fact", "Inference", "Judgment", "事实", "推断", "判断"),
}


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)


def assess_completion(
    body: str,
    facts: FactsPack,
    web_research_enabled: bool,
) -> tuple[ResearchStatus, list[str], dict[str, bool]]:
    checks = {
        name: _contains_any(body, markers)
        for name, markers in QUALITY_MARKERS.items()
    }
    checks["evidence_channel"] = bool(facts.facts) or web_research_enabled
    checks["substantive_output"] = len(body.strip()) >= 800

    gaps: list[str] = []
    labels = {
        "research_cutoff": "research cutoff 未明确",
        "industry": "行业分析结构缺失",
        "business_model": "商业模式分析结构缺失",
        "financial_quality": "财务质量分析结构缺失",
        "valuation": "估值分析结构缺失",
        "catalysts": "催化剂分析结构缺失",
        "risks": "风险分析结构缺失",
        "governance": "治理分析结构缺失",
        "final_view": "最终投资判断缺失",
        "thesis_break": "thesis-break / What Would Change My Mind 缺失",
        "five_metrics": "持续跟踪指标缺失",
        "unknowns": "Unknowns / Follow-up Diligence 缺失",
        "fact_inference_judgment": "事实 / 推断 / 判断的区分不够明确",
        "evidence_channel": "既无人工 facts pack，也未启用公开资料检索",
        "substantive_output": "报告正文过短，无法视为完整研究输出",
    }
    for name, passed in checks.items():
        if not passed:
            gaps.append(labels[name])

    if not checks["substantive_output"]:
        status: ResearchStatus = "BLOCKED"
    elif gaps:
        status = "COMPLETE_WITH_GAPS"
    else:
        status = "COMPLETE"

    return status, gaps, checks


def run_research(facts: FactsPack, peers: list[PeerItem], cfg: AgentConfig) -> ResearchOutput:
    prompt = build_user_prompt(
        facts,
        peers,
        web_research_enabled=cfg.enable_web_search,
    )
    body = run_llm(
        instructions=SYSTEM_PROMPT,
        prompt=prompt,
        model=cfg.model,
        reasoning_effort=cfg.reasoning_effort,
        enable_web_search=cfg.enable_web_search,
    )

    status, gaps, quality_checks = assess_completion(
        body,
        facts,
        web_research_enabled=cfg.enable_web_search,
    )

    if status == "COMPLETE":
        executive_summary = f"{facts.company} 的研究运行已结束；自动结构与证据通道检查通过。"
    elif status == "COMPLETE_WITH_GAPS":
        executive_summary = f"{facts.company} 的研究运行已结束，但仍有 {len(gaps)} 项非阻断质量或证据缺口，详见 Research Status。"
    else:
        executive_summary = f"{facts.company} 的研究运行遇到核心阻断，当前输出不足以视为完整研究报告。"

    return ResearchOutput(
        company=facts.company,
        ticker=facts.ticker,
        status=status,
        executive_summary=executive_summary,
        body_markdown=body,
        gaps=gaps,
        quality_checks=quality_checks,
        valuation_notes=build_valuation_skeleton(facts),
        comparable_notes=summarize_peers(peers),
    )
