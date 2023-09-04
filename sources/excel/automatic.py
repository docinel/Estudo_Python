import pyautogui as pa
import timeit
import openpyxl as xl

start_time = timeit.default_timer()

wb = xl.load_workbook(r'Z:\011-TI\017-BI_TESTES\BI_BASE_RELATORIOS\IMPL_SALDO.xlsx')
ws = wb['IMPL_SALDO']

meu_dic = {}
for cont in range(2, 3):
    meu_dic[f'A{cont}'] = ws[f'A{cont}'].value
    meu_dic[f'B{cont}'] = ws[f'B{cont}'].value

for cont in range(2, 3):
    # ABRE O MENTOR
    pa.hotkey('win', 'd')
    pa.sleep(1)
    pa.getWindowsWithTitle('Touch Comp ERP')[0].maximize()

    # NOVO ITEM
    pa.click(55, 296)
    pa.write(meu_dic[f'A{cont}'])
    pa.press('backspace')
    pa.press('enter')
    pa.sleep(1)
    pa.typewrite('3')
    pa.press('enter')
    pa.write(str(meu_dic[f'B{cont}']))
    pa.press('enter')
    pa.write('1')
    pa.press('enter', presses=3, interval=0.3)
    # print(meu_dic[f'A{cont}'])
    # print(meu_dic[f'B{cont}'])

print((timeit.default_timer() - start_time)/60)
