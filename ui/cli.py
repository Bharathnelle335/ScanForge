
import argparse
from scanners import SCANNER_MAP

def parse():
    p = argparse.ArgumentParser('scanforge')
    p.add_argument('target', help='source dir or image')
    for flag in SCANNER_MAP:
        p.add_argument(f'--{flag}', action='store_true')
    p.add_argument('--all', action='store_true')
    p.add_argument('--excel', action='store_true')
    p.add_argument('--dtrack', action='store_true')
    return p.parse_args()
