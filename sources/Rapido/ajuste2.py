import pyautogui as pa

pa.sleep(5)
start = 0
while start < 187:
    pa.typewrite('ok')
    pa.sleep(0.5)
    pa.press('down')
    start += 1