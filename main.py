from tkinter import *
from time import sleep


def lenght():
    global tam_linha
    tam_linha = int(caixa_01.get())
    play()


def step():
    global passo
    passo = int(caixa_02.get())
    play()


def background():
    global fundo
    fundo = caixa_03.get()
    play()


def char():
    global caractere
    caractere = caixa_04.get()
    play()


def speed():
    global tempo
    tempo = int(caixa_05.get()) * 0.05
    play()


def play():
    global tam_linha
    global passo
    global fundo
    global caractere
    global tempo

    regra = passo
    while True:
        for contador in range(1, tam_linha + 1):
            regra += 1
            if regra % passo == 0:
                print(caractere, end='')
            else:
                print(fundo, end='')
        print()
        sleep(tempo)


def clean():
    pass


janela = Tk()  # abre a janela
janela.title("KATSU")  # define o título da janela

# --------------------------------
# VARIÁVEIS GLOBAIS

tam_linha = 20  # define o tamanho de cada linha do desenho
passo = 7  # define quanto o pincel deve se deslocar entre as aparições
fundo = '0'  # define o caracter que representará o fundo do quadro
caractere = '1'  # define o caracter que represetará a tinta do pincel
tempo = 0.05  # define a velocidade com a qual o desenho se move

# --------------------------------
# WIDGETS

caixa_01 = Entry(janela)  # adicionar valor padrão "20"
caixa_02 = Entry(janela)  # adicionar valor padrão "7"
caixa_03 = Entry(janela)  # adicionar valor padrão "0"
caixa_04 = Entry(janela)  # adicionar valor padrão "1"
caixa_05 = Entry(janela)  # adicionar valor padrão "1"


botao_01 = Button(janela, text="Alterar a largura do quadro", command=lenght)
botao_02 = Button(janela, text="Alterar a pincelada", command=step)
botao_03 = Button(janela, text="Alterar a aparência do quadro", command=background)
botao_04 = Button(janela, text="Alterar a tinta", command=char)
botao_05 = Button(janela, text="Alterar a velocidade da obra", command=speed)  # speed = tempo * 0.05
botao_06 = Button(janela, text="Pintar", command=play)
botao_07 = Button(janela, text="Limpar o quadro", command=clean)

# --------------------------------
# Layout

caixa_01.grid(row=0, column=0, pady=5)
botao_01.grid(row=0, column=1, pady=5)
caixa_02.grid(row=1, column=0, pady=5)
botao_02.grid(row=1, column=1, pady=5)
caixa_03.grid(row=2, column=0, pady=5)
botao_03.grid(row=2, column=1, pady=5)
caixa_04.grid(row=3, column=0, pady=5)
botao_04.grid(row=3, column=1, pady=5)
caixa_05.grid(row=4, column=0, pady=5)
botao_05.grid(row=4, column=1, pady=5)
botao_06.grid(row=5, column=0, pady=5)
botao_07.grid(row=5, column=1, pady=5)


janela.mainloop()
