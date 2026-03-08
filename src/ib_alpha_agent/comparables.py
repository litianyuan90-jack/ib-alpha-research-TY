from __future__ import annotations
from statistics import median
from ib_alpha_agent.models import PeerItem

def summarize_peers(peers: list[PeerItem]) -> str:
    if not peers:
        return "未提供可比公司数据，无法做横向比较。"
    pe_values = [p.pe_ttm for p in peers if p.pe_ttm is not None]
    themes = ", ".join(sorted({p.theme for p in peers if p.theme}))
    if pe_values:
        med = median(pe_values)
        return f"已载入 {len(peers)} 家可比公司；主题覆盖：{themes or '未分类'}；PE(TTM)中位数约为 {med:.1f} 倍。"
    return f"已载入 {len(peers)} 家可比公司，但缺少足够的估值字段。"
