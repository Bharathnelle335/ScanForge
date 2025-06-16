
from core.scanner_base import ScannerBase
from output.normalizer import from_msbom

class MSBOMRunner(ScannerBase):
    TOOL = "MSBOM"

    def run(self):
        """Placeholder implementation — replace with real CLI calls."""
        # For now, we just return an empty structure.
        return {}

    def normalize(self, raw):
        return from_msbom(raw, origin=self.TOOL)
