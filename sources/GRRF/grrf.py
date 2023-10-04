from datetime import datetime
from time import strptime
import pyautogui as pa
import timeit
import openpyxl as xl
  
start_time = timeit.default_timer()

wb = xl.load_workbook(r'Z:\011-TI\017-BI_TESTES\BI_BASE_RELATORIOS\relatorio_auditor.xlsx')

ws = wb['GRRF']

qtd = int(pa.prompt(text='Digite a quantidade de Implantações:', title='QTD LINHAS' , default=''))
#  ABRE O MENTOR
pa.hotkey('win', 'd')
pa.sleep(1)
pa.getWindowsWithTitle('Touch Comp ERP')[0].maximize()

# NOVO ITEM
pa.doubleClick(1220, 164), pa.press('del'), pa.click(1220, 164)
meu_dic = {}
pa.sleep(5)
for cont in range(2, qtd):
    meu_dic[f'A{cont}'] = ws[f'A{cont}'].value
    meu_dic[f'B{cont}'] = ws[f'B{cont}'].value
    meu_dic[f'D{cont}'] = ws[f'D{cont}'].value

for cont in range(2, qtd):
    pa.write(str(meu_dic[f'A{cont}']))
    pa.sleep(1)
    pa.press('enter')
    pa.sleep(1)
    pa.click(1157, 429)
#     pa.typewrite('3')
    pa.sleep(1)
#     pa.press('enter')
    data = ws[f'D{cont}'].value
    data_t = datetime.date(data)
    data_te = format(data_t, '%d%m%Y')
    data_t_ano = format(data_t, '%Y')
    pa.write(data_te)
    pa.press('tab')
    pa.sleep(1)
    pa.press('enter')
    pa.sleep(3)
    pa.press('left')
    pa.write(str(meu_dic[f'B{cont}']))
    pa.write('_' + data_t_ano + '_')
    pa.press('enter', presses=3, interval=2)
    pa.doubleClick(1220, 164), pa.press('del'), pa.click(1220, 164)
#     pa.write('1')
#     pa.press('enter', presses=4, interval=0.3)

# # Finalizando e Salvando
# pa.click(681, 396)

print((timeit.default_timer() - start_time)/60)
