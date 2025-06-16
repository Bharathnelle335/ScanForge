
import os, requests, json

class DependencyTrackUploader:
    """Simplistic uploader — expects env vars DT_API_KEY and DT_URL."""
    def upload(self, bom_path: str):
        api_key = os.getenv('DT_API_KEY')
        base_url = os.getenv('DT_URL')
        if not api_key or not base_url:
            print('Dependency‑Track credentials not supplied; skipping.')
            return
        url = f"{base_url.rstrip('/')}/api/v1/bom"
        files = { 'bom': open(bom_path, 'rb') }
        headers = { 'X‑Api‑Key': api_key }
        resp = requests.post(url, headers=headers, files=files)
        resp.raise_for_status()
        print('Uploaded SBOM successfully')
