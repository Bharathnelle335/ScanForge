
from core.scanner_base import ScannerBase
from output.normalizer import from_ort

class ORTRunner(ScannerBase):
    TOOL = "ORT"

    def run(self):
        """Placeholder implementation — replace with real CLI calls."""
        # For now, we just return an empty structure.
        return {}

    def normalize(self, raw):
        return from_ort(raw, origin=self.TOOL)
