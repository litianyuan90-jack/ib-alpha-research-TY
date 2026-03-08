from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field

class FactsPack(BaseModel):
    company: str
    ticker: str | None = None
    sector: str | None = None
    facts: dict[str, Any] = Field(default_factory=dict)

class PeerItem(BaseModel):
    name: str
    ticker: str | None = None
    theme: str | None = None
    pe_ttm: float | None = None
    ev_ebitda: float | None = None

class ValuationSnapshot(BaseModel):
    method: str
    summary: str
    range_low: float | None = None
    range_base: float | None = None
    range_high: float | None = None

class ResearchOutput(BaseModel):
    company: str
    ticker: str | None = None
    executive_summary: str
    body_markdown: str
    valuation_notes: list[ValuationSnapshot] = Field(default_factory=list)
    comparable_notes: str | None = None
