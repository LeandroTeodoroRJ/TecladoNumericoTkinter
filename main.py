#*************************************************************************************************
#                                    Exemplo Teclado Numérico
#*************************************************************************************************
#INCLUDES
from tkinter import *
from tecladonumerico import TecladoNumerico as NumKey

#CONSTANTES E DEFINIÇÕES
resolucao = '300x300+200+200'
#FUNÇÕES
def clica_botao():
    numkey.open()

def clica_botao2():
    print(numkey.get_last_value())


#GUI
janela = Tk()
janela.geometry(resolucao)
bt = Button(janela, width=20, text='Abrir Teclado', command=clica_botao)
bt2 = Button(janela, width=20, text='Último Valor', command=clica_botao2)
ed1 = Entry(janela)
bt.grid(row=0, column=0)
ed1.grid(row=1, column=0)
bt2.grid(row=2, column=0)
numkey = NumKey(ed1)     #Instância do objeto Teclado Numérico
    
janela.mainloop()
