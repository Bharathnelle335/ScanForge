
"""Write combined scanner results to an Excel workbook."""
from openpyxl import Workbook

def write_excel(results, out_path='combined.xlsx'):
    wb = Workbook()
    wb.remove(wb.active)
    for res in results:
        ws = wb.create_sheet(res.get('origin', 'UNKNOWN'))
        ws.append(['components', 'licenses'])
        ws.append([str(res['components']), str(res['licenses'])])
    wb.save(out_path)
