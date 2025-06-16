
from core.scanner_base import ScannerBase
from output.normalizer import from_scanoss

class ScanossRunner(ScannerBase):
    TOOL = "SCANOSS"

    def run(self):
        """Placeholder implementation — replace with real CLI calls."""
        # For now, we just return an empty structure.
        return {}

    def normalize(self, raw):
        return from_scanoss(raw, origin=self.TOOL)
