from pathlib import Path

caminho_projeto = Path(__file__).parent.parent
print('------------------')
print(caminho_projeto)
print('------------------')
caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print('--------Arquivos----------')
proj = Path.home() / 'Documents' / 'Sources_Imagens'
arq = Path(__file__)
print(arq)
print('------------------')
print(Path.home() / 'PycharmProjects')
print('------------------')
print('------------------')
