import json, subprocess, tempfile, pathlib
from core.scanner_base import ScannerBase
from output.normalizer import from_syft

class SyftRunner(ScannerBase):
    TOOL = "SYFT"

    def run(self):
        tmp = pathlib.Path(tempfile.gettempdir()) / "syft.json"
        cmd = ["syft", str(self.target), "-o", "cyclonedx-json"]
        with tmp.open("w") as fp:
            subprocess.run(cmd, check=True, stdout=fp)
        return json.load(tmp.open())

    def normalize(self, raw):
        return from_syft(raw, origin=self.TOOL)
