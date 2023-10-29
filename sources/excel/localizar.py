import pyautogui as pa

pa.sleep(5)
novo = pa.locateCenterOnScreen(r'sources\excel\btNovo.png', confidence=0.9)
pa.click(novo)
# crhome = pa.locateCenterOnScreen(r'sources\excel\crhome.png', confidence=0.9)
# pa.doubleClick(crhome)
# pa.sleep(1)
# docinel = pa.locateCenterOnScreen(r'sources\excel\docinel.png',
# confidence=0.9)
# pa.click(docinel)
# encontrar = 'sim'

# while encontrar == 'sim':
#     try:
#         imagem = pa.locateCenterOnScreen(r'sources\excel\mensagem.png',
#                                          confidence=0.9)
#         pa.click(imagem)
#         pa.click(630, 444)
#     except Exception:
#         print('Não Encontrado')
