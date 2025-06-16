
"""Scanner registry for ScanForge."""
from .scanoss_runner import ScanossRunner
from .ort_runner import ORTRunner
from .syft_runner import SyftRunner
from .scancode_runner import ScanCodeRunner
from .msbom_runner import MSBOMRunner

SCANNER_MAP = {
    'scanoss': ScanossRunner,
    'ort': ORTRunner,
    'syft': SyftRunner,
    'scancode': ScanCodeRunner,
    'msbom': MSBOMRunner,
}
