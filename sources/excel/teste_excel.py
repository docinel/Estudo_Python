import openpyxl as xl

calculo = 1.5

wb = xl.load_workbook(r'sources/excel/calculo.xlsx')
sheet = wb['Plan1']

for rows in sheet.iter_rows(min_row=2, max_row=3):
    for cell in rows:
        print(cell.value)

coluna_alvo = "A"
linha_alvo = 2

celula = f'{coluna_alvo}{linha_alvo}'

valor = sheet[celula].value
wb.close()

print(valor * calculo)

