
import win32gui
import time
import pyautogui as pa


time.sleep(10)

w = win32gui
window = win32gui.GetWindowText(w.GetForegroundWindow())

pa.click(729, 68)
pa.write('helo')       
print(window)
