from __future__ import annotations
from ib_alpha_agent.models import FactsPack, ValuationSnapshot

def build_valuation_skeleton(facts: FactsPack) -> list[ValuationSnapshot]:
    sector = (facts.sector or "").lower()
    out = [ValuationSnapshot(method="PE / EV-EBITDA", summary="先用相对估值观察市场给出的交易现实，再校正一次性收益影响。")]
    if "idc" in sector or "aidc" in sector or "基础设施" in (facts.sector or ""):
        out.append(ValuationSnapshot(method="SOTP", summary="对 IDC/AIDC、增值服务、REIT资产循环分部估值，避免只看表观PE。"))
        out.append(ValuationSnapshot(method="DCF", summary="对成熟机柜、上架率、功率密度、资本开支和现金流进行折现。"))
    else:
        out.append(ValuationSnapshot(method="DCF", summary="用核心经营现金流而非报表噪音利润作为内在价值锚。"))
    return out
