
from ui.cli import parse
from scanners import SCANNER_MAP
from output.excel_writer import write_excel
from scanners.dtrack_runner import DependencyTrackUploader
import traceback

def run_selected_scanners(target, selected_flags):
    results = []
    summary = []
    for flag in selected_flags:
        runner_cls = SCANNER_MAP[flag]
        runner = runner_cls(target)
        print(f"▶ Running {flag.upper()}...")
        try:
            raw = runner.run()
            normalized = runner.normalize(raw)
            results.append(normalized)
            summary.append((flag.upper(), "✔ Success", f"{len(normalized.get('components', []))} components"))
        except Exception as e:
            err = traceback.format_exc(limit=1).strip().splitlines()[-1]
            print(f"✖ {flag.upper()} failed: {err}")
            summary.append((flag.upper(), "✖ Failed", str(err)))
    return results, summary

def print_summary(summary):
    print("\n======= ScanForge Summary =======")
    for tool, status, info in summary:
        print(f"{status} {tool}: {info}")
    print("=================================\n")

def main():
    args = parse()
    flags = list(SCANNER_MAP.keys()) if args.all else [f for f in SCANNER_MAP if getattr(args, f)]
    results, summary = run_selected_scanners(args.target, flags)
    print_summary(summary)

    if args.excel:
        write_excel(results, 'combined.xlsx', summary)

    if args.dtrack and args.target.endswith(('.xml', '.json')):
        DependencyTrackUploader().upload(args.target)
    elif args.dtrack:
        DependencyTrackUploader().upload('combined.xml')

    # Exit with error if ALL scanners failed
    if all(s[1].startswith('✖') for s in summary):
        exit(1)

if __name__ == '__main__':
    main()
