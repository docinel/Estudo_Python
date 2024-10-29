# Barra de Progresso

from tkinter import *
from tkinter.ttk import *
import time

janela = Tk()

barra_progresso = Progressbar(janela, orient=HORIZONTAL, length=300, mode='determinate')
barra_progresso.pack()
barra_progresso.start(10)
janela.mainloop()

