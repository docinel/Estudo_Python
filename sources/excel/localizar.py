import pyautogui as pa
from pathlib import Path
import cv2

pa.FAILSAFE = True

pa.sleep(3)
# novo = pa.locateCenterOnScreen(r'sources\excel\btNovo.png', confidence=0.9)
# pa.click(novo)
excel = pa.locateAllOnScreen(r'C:\Users\rodrigo.docinel\Documents\Sources_Imagens\excel.png', confidence=0.9)
pa.sleep(1)
pa.click(excel.x, excel.y)
# crhome = pa.locateCenterOnScreen(r'sources\excel\crhome.png', confidence=0.9)
# pa.doubleClick(crhome)
# pa.sleep(1)
# docinel = pa.locateCenterOnScreen(r'sources\excel\docinel.png',
# confidence=0.9)
# pa.click(docinel)

# with open(r'C:\Users\rodrigo.docinel\Documents\Sources_Imagens\excel.png', 'rb') as imagem:
#     imagem = pa.locateCenterOnScreen(imagem, confidence=0.9)
#     pa.click(imagem)

# caminho_imagens = Path.home() / 'Documents' / 'Sources_Imagens'
# print(caminho_imagens)
# with open (caminho_imagens / 'excel.png', 'rb') as imagem:
#     imagem = pa.locateCenterOnScreen(imagem, confidence=0.9)
#     pa.click(imagem)

# caminho_imagens = Path.home() / 'Documents' / 'Sources_Imagens'
# print(caminho_imagens)
# encontrar = 'sim'

# while encontrar == 'sim':
#     try:
#         imagem = pa.locateCenterOnScreen(f'{caminho_imagens}' / 'excel.png', confidence=0.9)
#         pa.click(imagem.x, imagem.y)
#         encontrar = 'nao'
#     except Exception:
#         break
           