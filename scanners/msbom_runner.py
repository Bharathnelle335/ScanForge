import json, subprocess, tempfile, pathlib
from core.scanner_base import ScannerBase
from output.normalizer import from_msbom

class MSBOMRunner(ScannerBase):
    TOOL = "MSBOM"

    def run(self):
        tmp = pathlib.Path(tempfile.gettempdir()) / "msbom.json"
        cmd = [
            "sbom-tool", "generate",
            "-b", str(self.target),
            "-bc", ".", "-pn", "ScanForge", "-pv", "1.0",
            "-ps", "ScanForge",
            "-nsb", "true",          # produce CycloneDX JSON
            "-o", str(tmp)
        ]
        subprocess.run(cmd, check=True)
        return json.load(tmp.open())

    def normalize(self, raw):
        return from_msbom(raw, origin=self.TOOL)
