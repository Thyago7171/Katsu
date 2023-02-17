from time import sleep

tam_linha = 20  # define o tamanho de cada linha do desenho
passo = 7  # define quanto o pincel deve se deslocar entre as aparições
fundo = '0'  # define o caracter que representará o fundo do quadro
caractere = '1'  # define o caracter que represetará a tinta do pincel
tempo = 0.05  # define a velocidade com a qual o desenho se move

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
