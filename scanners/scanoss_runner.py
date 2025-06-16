import json, subprocess, tempfile, pathlib
from core.scanner_base import ScannerBase
from output.normalizer import from_scanoss

class ScanossRunner(ScannerBase):
    TOOL = "SCANOSS"

    def run(self):
        tmp = pathlib.Path(tempfile.gettempdir()) / "scanoss.json"
        cmd = ["scanoss", "scan", str(self.target)]
        with tmp.open("w") as fp:
            subprocess.run(cmd, check=True, stdout=fp)
        return json.load(tmp.open())

    def normalize(self, raw):
        return from_scanoss(raw, origin=self.TOOL)
