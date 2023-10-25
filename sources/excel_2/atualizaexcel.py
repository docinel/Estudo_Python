import win32com.client
import pyautogui as pa
import timeit
import pygetwindow as pg

start_time = timeit.default_timer()

arquivo = win32com.client.Dispatch("Excel.Application")

arquivo.Visible = 1

planilha = arquivo.Workbooks.open(r"Z:\011-TI\017-BI_TESTES\VENDAS_MENSAIS\BASE_MENSAL.xlsm")
pa.sleep(10)
pa.hotkey('win', 'd')
pa.sleep(2)
pg.getWindowsWithTitle('BASE_MENSAL.xlsm - Excel')[0].maximize()
pa.sleep(2)
planilha.RefreshAll()
pa.sleep(5)
planilha.RefreshAll()
pa.sleep(10)
pa.hotkey('alt', 'f4')
pa.press('l')
tempo = (timeit.default_timer() - start_time)/60
tempo_texto = str(tempo)
pa.alert(text=f'O Tempo gasto foi de: {tempo_texto}',
         title='teeste', button='OK')
