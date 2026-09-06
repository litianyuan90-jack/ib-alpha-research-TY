from __future__ import annotations
import json
from pathlib import Path
from ib_alpha_agent.models import FactsPack, PeerItem

ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = ROOT / "SKILL.md"


def load_system_prompt() -> str:
    if not SKILL_PATH.exists():
        raise FileNotFoundError(
            f"Canonical research skill not found at {SKILL_PATH}. "
            "Run the agent from a checkout that contains the repository-level SKILL.md."
        )
    return SKILL_PATH.read_text(encoding="utf-8").strip()


SYSTEM_PROMPT = load_system_prompt()


def build_user_prompt(
    facts: FactsPack,
    peers: list[PeerItem],
    web_research_enabled: bool = True,
) -> str:
    peers_text = "\n".join(
        f"- {p.name} ({p.ticker or 'N/A'}), theme={p.theme or 'N/A'}, "
        f"PE={p.pe_ttm if p.pe_ttm is not None else 'N/A'}, "
        f"EV/EBITDA={p.ev_ebitda if p.ev_ebitda is not None else 'N/A'}"
        for p in peers
    ) or "无可比公司数据"

    facts_text = json.dumps(facts.facts, ensure_ascii=False, indent=2) if facts.facts else "未提供人工 facts pack"

    if web_research_enabled:
        evidence_instruction = """
公开资料检索已启用。请先自主补齐完成判断所需的 evidence pack，再形成结论。
优先检索公司公告、交易所披露、年报/季报、官方 IR、监管/政策文件与可比公司官方披露。
不要因为缺少人工 facts pack 而停止；无法验证的信息标记为 Unknown / Verify，并降低置信度。
""".strip()
    else:
        evidence_instruction = """
公开资料检索未启用。仅使用提供的事实包与模型已有知识；对时效性或无法验证的信息必须明确标记 Unknown / Verify。
不要用猜测填补证据缺口。
""".strip()

    return f"""
请按仓库根目录 `SKILL.md` 的完整方法论，生成一份机构级中文股票研究报告。

目标公司：
- 公司：{facts.company}
- 代码：{facts.ticker or 'N/A'}
- 赛道：{facts.sector or 'N/A'}

人工事实包：
{facts_text}

可比公司输入：
{peers_text}

证据获取规则：
{evidence_instruction}

执行要求：
- 完整执行 SKILL.md 的 Required output structure 与 Quality gate。
- 明确 research cutoff。
- 将事实、推断、判断区分清楚。
- 缺少非关键证据时继续完成可完成部分，并在 Unknowns / Follow-up Diligence 中列出缺口。
- 不要仅因存在资料缺口而向用户索取补充；只有真正阻断核心结论的缺口才应标记为 BLOCKED。
- 不得在正文中声称“研究已完成”来替代质量检查。
""".strip()
