import pyautogui as pa
from pathlib import Path

pa.FAILSAFE = True

pa.sleep(3)
# novo = pa.locateCenterOnScreen(r'sources\excel\btNovo.png', confidence=0.9)
# pa.click(novo)
# excel = pa.locateAllOnScreen(r'sources\excel2\excel.png', confidence=0.9)
# pa.sleep(1)
# pa.moveTo(excel)
# crhome = pa.locateCenterOnScreen(r'sources\excel\crhome.png', confidence=0.9)
# pa.doubleClick(crhome)
# pa.sleep(1)
# docinel = pa.locateCenterOnScreen(r'sources\excel\docinel.png',
# confidence=0.9)
# pa.click(docinel)
caminho_imagens = Path.home() / 'Documents' / 'Sources_Imagens'
encontrar = 'sim'

while encontrar == 'sim':
    try:
        imagem = pa.locateCenterOnScreen(caminho_imagens / 'btNovo.png', confidence=0.9)
        pa.click(imagem)
        encontrar = 'nao'
    except Exception:
        print('Não Encontrado')
