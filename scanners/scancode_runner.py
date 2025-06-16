import json, subprocess, tempfile, pathlib, os
from core.scanner_base import ScannerBase
from output.normalizer import from_scancode

class ScanCodeRunner(ScannerBase):
    TOOL = "SCANCODE"

    def run(self):
        tmp = pathlib.Path(tempfile.gettempdir()) / "scancode.json"
        project = pathlib.Path(self.target).resolve()
        cmd = [
            "docker", "run", "--rm",
            "-v", f"{project}:/src",
            "aboutcode/scancode-toolkit:33.0.3",
            "-clp", "--json-pp", "/tmp/out.json", "/src"
        ]
        subprocess.run(cmd, check=True)
        # copy back
        subprocess.run(["docker", "cp", "$(docker ps -ql):/tmp/out.json", str(tmp)])
        return json.load(tmp.open())

    def normalize(self, raw):
        return from_scancode(raw, origin=self.TOOL)
