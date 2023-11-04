import pyautogui as pa
import timeit
import webbrowser
from pathlib import Path

start_time = timeit.default_timer()

caminho_arquivo = Path.home() / 'Documents' / 'Sources_Imagens'

pa.hotkey('win', 'd')
pa.sleep(1)

pa.hotkey('win', 'r')
pa.sleep(1)
pa.typewrite(r"Z:\011-TI\017-BI_TESTES\BI_BASE_RELATORIOS\BASE.xlsm")
pa.sleep(1)
pa.press('enter')
pa.sleep(20)

pa.hotkey('ctrl', 'h')
pa.sleep(2)

pa.hotkey('win', 'd')
pa.sleep(1)
webbrowser.open('https://docs.google.com/spreadsheets/d/14x5Mep-8uO31VahOrhBd24ZslE6L_Bmk8IJU15WrazY/edit?usp=sharing')
pa.sleep(20)
pa.hotkey('ctrl', 'shift', 'v')
pa.sleep(60)
pa.hotkey('win', 'd')
pa.sleep(1)

excel = pa.locateCenterOnScreen(caminho_arquivo / 'excel.png', confidence=0.9)
# excel = pa.locateCenterOnScreen("C:\\Users\\narobo\\Documents\\Estudo_Python\\sources\\excel_2\\excel.png", confidence=0.9)
pa.sleep(1)
pa.click(excel)
pa.sleep(1)
pa.click(55, 296)
pa.sleep(1)
pa.hotkey('alt', 'f4')
pa.sleep(3)
pa.press('l')
pa.sleep(3)
pa.press('n')
pa.sleep(5)
try:
    google_2 = pa.locateCenterOnScreen(caminho_arquivo / 'google_2.png', confidence=0.9)
    # google_2 = pa.locateCenterOnScreen("C:\\Users\\narobo\\Documents\\Estudo_Python\\sources\\excel_2\\google_2.png", confidence=0.9)
    pa.sleep(2)
    pa.click(google_2)
    pa.sleep(3)
    pa.hotkey('ctrl', 'w')
except Exception:
    google = pa.locateCenterOnScreen(caminho_arquivo / 'google.png', confidence=0.9)
    # google = pa.locateCenterOnScreen("C:\\Users\\narobo\\Documents\\Estudo_Python\\sources\\excel_2\\google.png", confidence=0.9)
    pa.sleep(2)
    pa.click(google)
    pa.sleep(3)
    pa.hotkey('ctrl', 'w')

print((timeit.default_timer() - start_time)/60)
