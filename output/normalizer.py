
"""Utility functions that map each tool's raw output into a shared schema.
Very minimal for the skeleton — extend as you add real parsers.
"""
def _base(origin: str):
    return {'components': [], 'licenses': [], 'origin': origin}

def from_syft(raw, origin='SYFT'):
    return _base(origin)

def from_scanoss(raw, origin='SCANOSS'):
    return _base(origin)

def from_ort(raw, origin='ORT'):
    return _base(origin)

def from_scancode(raw, origin='SCANCODE'):
    return _base(origin)

def from_msbom(raw, origin='MSBOM'):
    return _base(origin)
