import pyautogui as pa

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
encontrar = 'sim'

while encontrar == 'sim':
    try:
        imagem = pa.locateCenterOnScreen(r'sources\excel_2\excel.png',
                                         confidence=0.9)
        pa.click(imagem)
        encontrar = 'nao'
    except Exception:
        print('Não Encontrado')
