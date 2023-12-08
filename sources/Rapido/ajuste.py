import pyautogui as pa

pa.FAILSAFE = True

pa.sleep(5)
# pa.press('enter', presses=5, interval=0.2)
inicio = 0
while inicio < 18:
    seq = 31
    pa.press('F2')
    pa.press('backspace', presses=2, interval=0.2)
    num = seq + inicio
    pa.typewrite(f'{num}')
    pa.press('enter')
    # pa.press('left', presses=3, interval=0.2)
    # pa.press('backspace')
    # pa.typewrite('2')
    # pa.hotkey('ctrl', 'left')
    # pa.sleep(0.5)
    # pa.press('backspace')
    # pa.press('enter')
#     # *******************************************************************************
#     # pa.press('F2')
#     # pa.press('left', presses=9, interval=0.2)
#     # pa.press('backspace')
#     # pa.press('left', presses=2, interval=0.2)
#     # pa.press('backspace')
#     # pa.press('enter')
    inicio += 1


# for num in range(1, 6):
#     pa.press('F2')
#     pa.press('backspace', presses=2, interval=0.2)
#     seq = 19
#     pa.write({seq} + 1)
#     pa.press('enter')
