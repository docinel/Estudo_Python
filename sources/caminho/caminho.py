from pathlib import Path, PureWindowsPath
import pyautogui as pa

caminho_projeto = Path(__file__).parent.parent
print('------------------')
print(caminho_projeto)
print('------------------')
caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print('--------Arquivos----------')
proj = Path.home() / 'Documents' / 'Sources_Imagens' / 'excel.png'
print(proj)
arq = Path(__file__)
print(arq)
print('------------------')
print(Path.home() / 'PycharmProjects')
print('------------------')
print('------------------')

pa.locateCenterOnScreen(proj, confidence=0.9)
pa.click(pa.locateCenterOnScreen(proj, confidence=0.9))


