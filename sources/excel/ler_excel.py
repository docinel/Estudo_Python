import openpyxl as xl

wb = xl.load_workbook(r'sources/excel/calculo.xlsx')
ws = wb.active

# print(wb.sheetnames)
for row in ws.iter_rows(min_row=2, values_only=True):
    for cell in row:
        print(cell)


# celula = ws['A2']
# celula2 = ws['B2']

# print(celula.value)
# print(celula2.value)