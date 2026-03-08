from __future__ import annotations
from ib_alpha_agent.models import FactsPack, PeerItem

SYSTEM_PROMPT = '''
你是 IB Alpha Agent v3，一名机构级股票研究员。
请使用投行 + 科技成长基金的框架进行研究。
你的任务是判断：
1. 是不是好行业
2. 是不是好公司
3. 现在是不是好价格
4. 现在是不是好时点

强制要求：
- 区分事实、推断、判断
- 区分经常性与非经常性收益
- 对重资产行业，不得只看PE
- 重点输出：行业、商业模式、护城河、财务质量、估值、催化剂、风险、治理、结论
- 最后给出5个持续跟踪指标
'''.strip()

def build_user_prompt(facts: FactsPack, peers: list[PeerItem]) -> str:
    peers_text = "\n".join(
        f"- {p.name} ({p.ticker or 'N/A'}), theme={p.theme or 'N/A'}, PE={p.pe_ttm or 'N/A'}, EV/EBITDA={p.ev_ebitda or 'N/A'}"
        for p in peers
    ) or "无可比公司数据"
    return f'''
请基于以下事实包，生成一份机构级中文股票研究报告。

目标公司：
- 公司：{facts.company}
- 代码：{facts.ticker or 'N/A'}
- 赛道：{facts.sector or 'N/A'}

事实包：
{facts.facts}

可比公司：
{peers_text}

输出要求：
1. Executive Summary
2. Industry & Policy
3. Business Model
4. Competitive Position
5. Financial Quality
6. Valuation
7. Catalysts
8. Risks
9. Management & Governance
10. Final View
11. What Would Change My Mind
12. Five Metrics to Monitor
'''.strip()
