from __future__ import annotations
from typing import Protocol
from ib_alpha_agent.models import FactsPack, PeerItem

class FactsSource(Protocol):
    def load_facts(self, path: str) -> FactsPack: ...

class PeersSource(Protocol):
    def load_peers(self, path: str) -> list[PeerItem]: ...
