import json, subprocess, tempfile, pathlib, os
from core.scanner_base import ScannerBase
from output.normalizer import from_ort

ORT_JAR = "/usr/local/bin/ort.jar"  # path set in Dockerfile earlier

class ORTRunner(ScannerBase):
    TOOL = "ORT"

    def run(self):
        work = pathlib.Path(tempfile.mkdtemp())
        cmd = ["java", "-Xmx4g", "-jar", ORT_JAR,
               "analyze", "-i", str(self.target), "-o", str(work)]
        subprocess.run(cmd, check=True)
        result = json.load((work / "analyzer-result.json").open())
        return result

    def normalize(self, raw):
        return from_ort(raw, origin=self.TOOL)
