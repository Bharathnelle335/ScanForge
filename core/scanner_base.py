
"""Base class for every scanner in ScanForge."""
from abc import ABC, abstractmethod
from pathlib import Path
import typing as _t

class ScannerBase(ABC):
    def __init__(self, target: str, **cfg):
        self.target = Path(target)
        self.cfg = cfg

    @abstractmethod
    def run(self) -> dict:
        """Run the scanner and return raw output as Python data (JSON‑like)."""
        ...

    @abstractmethod
    def normalize(self, raw: dict) -> dict:
        """Convert *raw* output into a CycloneDX‑compatible dict."""
        ...
