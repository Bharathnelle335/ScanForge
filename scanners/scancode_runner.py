
from core.scanner_base import ScannerBase
from output.normalizer import from_scancode

class ScanCodeRunner(ScannerBase):
    TOOL = "SCANCODE"

    def run(self):
        """Placeholder implementation — replace with real CLI calls."""
        # For now, we just return an empty structure.
        return {}

    def normalize(self, raw):
        return from_scancode(raw, origin=self.TOOL)
