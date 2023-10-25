import pyautogui as pa


pa.FAILSAFE = True

pa.sleep(5)

# Pega a posição do mouse
print(pa.position())
# Pega o tamanho da tela
print(pa.size())

# Move o mouse para a coordenada (x, y) durante 3 segundos
pa.moveTo(100, 100, 3)

# Move o mouse para a posição atual do mouse
pa.moveRel(100, 150, 3)

