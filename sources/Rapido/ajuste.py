import pyautogui as pa

pa.sleep(5)
inicio = 0
while inicio < 16:
    pa.press('F2')
    pa.hotkey('ctrl', 'left')
    pa.sleep(0.5)
    pa.press('backspace')
    pa.press('enter')
    # *******************************************************************************
    # pa.press('F2')
    # pa.press('left', presses=9, interval=0.2)
    # pa.press('backspace')
    # pa.press('left', presses=2, interval=0.2)
    # pa.press('backspace')
    # pa.press('enter')
    inicio += 1
