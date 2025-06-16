
import subprocess, shlex

def run_docker(image: str, cmd: str, mounts=None):
    mounts = mounts or {}
    mount_flags = ' '.join(f"-v {host}:{cont}" for host, cont in mounts.items())
    full_cmd = f"docker run --rm {mount_flags} {image} {cmd}"
    subprocess.run(shlex.split(full_cmd), check=True)
