from __future__ import annotations
from ib_alpha_agent.models import FactsPack, PeerItem
from ib_alpha_agent.utils import read_json

def load_facts_pack(path: str) -> FactsPack:
    return FactsPack.model_validate(read_json(path))

def load_peers_pack(path: str | None) -> list[PeerItem]:
    if not path:
        return []
    return [PeerItem.model_validate(x) for x in read_json(path)]
