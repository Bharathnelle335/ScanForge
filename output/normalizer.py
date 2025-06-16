"""
Map each scanner’s native JSON into a shared dict:

{
  "origin": "SYFT",
  "components": [ {"name": "...", "version": "...", "purl": "..."} ],
  "licenses":  [ {"id": "MIT", "component": "purl"} ]
}
A minimalist pass-through so Excel isn’t empty.
"""
from typing import List, Dict

def _base(origin: str) -> Dict:
    return {"origin": origin, "components": [], "licenses": []}

# ---------- Syft & MS SBOM (CycloneDX JSON) ----------
def _from_cyclonedx(raw: Dict, origin: str) -> Dict:
    doc = _base(origin)
    for c in raw.get("components", []):
        doc["components"].append(
            {
                "name":    c.get("name"),
                "version": c.get("version"),
                "purl":    c.get("purl"),
            }
        )
        for lic in (c.get("licenses") or []):
            doc["licenses"].append(
                {
                    "id": lic.get("license", {}).get("id") or lic.get("expression"),
                    "component": c.get("purl"),
                }
            )
    return doc

def from_syft(raw, origin="SYFT"):
    return _from_cyclonedx(raw, origin)

def from_msbom(raw, origin="MSBOM"):
    return _from_cyclonedx(raw, origin)

# ---------- ScanOSS ----------
def from_scanoss(raw, origin="SCANOSS"):
    doc = _base(origin)
    for match in raw.get("matches", []):
        c = match.get("component", {})
        doc["components"].append(
            {"name": c.get("name"), "version": c.get("version")}
        )
        doc["licenses"].append(
            {"id": match.get("license"), "component": c.get("name")}
        )
    return doc

# ---------- ScanCode ----------
def from_scancode(raw, origin="SCANCODE"):
    doc = _base(origin)
    for file_ in raw.get("files", []):
        for pkg in file_.get("packages", []):
            doc["components"].append(
                {"name": pkg.get("name"), "version": pkg.get("version")}
            )
            for lic in pkg.get("licenses", []):
                doc["licenses"].append(
                    {"id": lic.get("key"), "component": pkg.get("name")}
                )
    return doc

# ---------- ORT ----------
def from_ort(raw, origin="ORT"):
    doc = _base(origin)
    for proj in raw.get("analyzer", {}).get("result", {}).get("projects", []):
        doc["components"].append(
            {"name": proj.get("id", {}).get("name"),
             "version": proj.get("id", {}).get("version")}
        )
        for lic in proj.get("declaredLicenses", []):
            doc["licenses"].append({"id": lic, "component": proj["id"]["name"]})
    return doc
