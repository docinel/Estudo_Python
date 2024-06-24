import openpyxl as xl

wb = xl.load_workbook(r'sources\Fech_os\Pasta1.xlsx')
ws = wb.active


for row in ws.iter_rows(min_row=2, values_only=True):
    for cell in row:
        print(cell)
