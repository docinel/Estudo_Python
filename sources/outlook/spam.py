import pyautogui as pa
import openpyxl as xl
import clipboard

pa.hotkey('win', 'r'), pa.typewrite('outlook'), pa.sleep(1), pa.press('enter')
pa.sleep(5), pa.click(110, 220), pa.sleep(1)
pa.click(404, 185), pa.sleep(0.5)
pa.rightClick(911, 126), pa.sleep(2), 
copia = pa.typewrite('p')
wb = xl.load_workbook(r'C:\workspaces\Estudo_Python\sources\outlook\spam.xlsx')
ws = wb['base']
ws.cell(row=1, column=1, value=copia)

