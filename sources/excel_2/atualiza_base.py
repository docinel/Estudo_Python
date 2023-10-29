import pyautogui as pa
import timeit
import webbrowser
import pygetwindow as pg

start_time = timeit.default_timer()

pa.hotkey('win', 'd')
pa.sleep(1)

pa.hotkey('win', 'r')
pa.sleep(1)
pa.typewrite(r"Z:\011-TI\017-BI_TESTES\BI_BASE_RELATORIOS\BASE.xlsm")
pa.sleep(1)
pa.press('enter')
pa.sleep(10)

pa.hotkey('ctrl', 'h')
pa.sleep(1)

pa.hotkey('win', 'd')
pa.sleep(1)
webbrowser.open('https://docs.google.com/spreadsheets/d/14x5Mep-8uO31VahOrhBd24ZslE6L_Bmk8IJU15WrazY/edit?usp=sharing')
pa.sleep(20)
pa.hotkey('ctrl', 'shift', 'v')
pa.sleep(35)
pa.hotkey('win', 'd')
pa.sleep(1)
excel = pa.locateAllOnScreen(r'sources\excel\excel.png', confidence=0.9, region=(0, 0, 1280, 720))
pa.sleep(1)
pa.click(excel)
pa.click(55, 296)
pa.hotkey('alt', 'f4')
pa.press('l')
pa.press('n')


# pa.hotkey('ctrl', 'shift', 'right')

print((timeit.default_timer() - start_time)/60)
