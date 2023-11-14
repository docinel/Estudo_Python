import pyautogui as pa

pa.FAILSAFE = True


pa.sleep(5)

texto = open('sources\Pyautogui\Fail_safe.txt')
linha = 'helo'
for linha in texto:
    pa.write(linha)