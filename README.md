
**Work in Progress**
# ScanForge

**ScanForge** is a unified OSS scanning orchestrator that glues together Syft, SCANOSS, ScanCode Toolkit, ORT, Microsoft SBOM tool, and Dependency‑Track in one command‑line.

```bash
# Native usage
python main.py --scanoss --syft --excel /path/to/source

# Run everything
python main.py --all --excel --dtrack .
```

## Features

* Modular scanner runners
* Normalized CycloneDX schema across tools
* Excel report generator
* Optional Dependency‑Track uploader
* Works locally or in GitHub Actions

See `.github/workflows/oss-scan.yml` for CI example.
