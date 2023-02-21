from tkinter import *
import os
from time import sleep


# Altera a quantidade de caracteres por linha
def lenght():
    global tam_linha
    tam_linha = int(caixa_01.get())


# Altera a quantidade de linhas
def height():
    global quant_linha
    quant_linha = int(caixa_02.get())


# Altera o espaçamento entre a variação de caracter utilizado
def step():
    global passo
    passo = int(caixa_03.get())


# Altera o caracter padrão
def background():
    global fundo
    fundo = caixa_04.get()


# Altera o caracter especial
def char():
    global caractere
    caractere = caixa_05.get()


# Altera o tempo de sleep
def speed():
    global tempo
    tempo = 0.05 / float(caixa_06.get())  # Calcula o tempo inversamente proporcional à velocidade


# Executa o print resultado dos valores escolhidos
def play():
    global tam_linha
    global quant_linha
    global passo
    global fundo
    global caractere
    global tempo

    regra = passo
    for contador_01 in range(1, quant_linha + 1):
        for contador_02 in range(1, tam_linha + 1):
            regra += 1
            if regra % passo == 0:
                print(caractere, end='')
            else:
                print(fundo, end='')
        print()
        sleep(tempo)


# Limpa o terminal
def clean():
    os.system('cls')


janela = Tk()  # abre a janela
janela.title("KATSU")  # define o título da janela

# --------------------------------
# VARIÁVEIS GLOBAIS

tam_linha = 20  # define o tamanho de cada linha do desenho
quant_linha = 100  # define a quantidade de linhas do desenho
passo = 21  # define quanto o pincel deve se deslocar entre as aparições
fundo = '0'  # define o caracter que representará o fundo do quadro
caractere = '1'  # define o caracter que represetará a tinta do pincel
tempo = 0.05  # define a velocidade com a qual o desenho se move

# --------------------------------
# WIDGETS

caixa_01 = Entry(janela)
caixa_01.insert(END, "20")
caixa_02 = Entry(janela)
caixa_02.insert(END, "100")
caixa_03 = Entry(janela)
caixa_03.insert(END, "7")
caixa_04 = Entry(janela)
caixa_04.insert(END, "0")
caixa_05 = Entry(janela)
caixa_05.insert(END, "1")
caixa_06 = Entry(janela)
caixa_06.insert(END, "1")


botao_01 = Button(janela, text="Alterar a largura do quadro", command=lenght)
botao_02 = Button(janela, text="Alterar a altura do quadro", command=height)
botao_03 = Button(janela, text="Alterar a pincelada", command=step)
botao_04 = Button(janela, text="Alterar a aparência do quadro", command=background)
botao_05 = Button(janela, text="Alterar a tinta", command=char)
botao_06 = Button(janela, text="Alterar a velocidade da obra", command=speed)
botao_07 = Button(janela, text="Pintar", command=play)
botao_08 = Button(janela, text="Limpar o quadro", command=clean)

# --------------------------------
# LAYOUT

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
caixa_06.grid(row=5, column=0, pady=5)
botao_06.grid(row=5, column=1, pady=5)
botao_07.grid(row=6, column=0, pady=5)
botao_08.grid(row=6, column=1, pady=5)


janela.mainloop()
