
from ui.cli import parse
from scanners import SCANNER_MAP
from output.excel_writer import write_excel
from scanners.dtrack_runner import DependencyTrackUploader

def run_selected_scanners(target, selected_flags):
    results = []
    for flag in selected_flags:
        runner_cls = SCANNER_MAP[flag]
        runner = runner_cls(target)
        raw = runner.run()
        results.append(runner.normalize(raw))
    return results

def main():
    args = parse()
    flags = list(SCANNER_MAP.keys()) if args.all else [f for f in SCANNER_MAP if getattr(args, f)]
    results = run_selected_scanners(args.target, flags)
    if args.excel:
        write_excel(results, 'combined.xlsx')
    if args.dtrack:
        DependencyTrackUploader().upload('combined.xml')
    print('ScanForge finished')

if __name__ == '__main__':
    main()
