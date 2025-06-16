
from core.scanner_base import ScannerBase
from output.normalizer import from_syft

class SyftRunner(ScannerBase):
    TOOL = "SYFT"

    def run(self):
        """Placeholder implementation — replace with real CLI calls."""
        # For now, we just return an empty structure.
        return {}

    def normalize(self, raw):
        return from_syft(raw, origin=self.TOOL)
