import pyautogui as pa

pa.sleep(5)
encontrar = 'sim'

while encontrar == 'sim':
    try:
        imagem = pa.locateCenterOnScreen(r'sources\excel\mensagem.png',
                                         confidence=0.9)
        pa.click(imagem)
        pa.click(630, 444)
    except Exception:
        print('Não Encontrado')
