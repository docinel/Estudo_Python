import pyautogui as pa


pa.sleep(5)
pa.press('enter', presses=5, interval=0.2)
inicio = 0
while inicio < 10:
    seq = 467
    pa.press('F2')
    pa.press('backspace', presses=3, interval=0.2)
    inicio += 1
    num = seq + inicio
    pa.typewrite(f'{num}')
    pa.press('enter')

