from time import sleep

tam_linha = 20
quant_linhas = 30
passo = 7
fundo = '0'
caractere = '1'
tempo = 0.05


regra = passo
while True:
    for d in range(1, tam_linha + 1):
        regra += 1
        if regra % passo == 0:
            print(caractere, end='')
        else:
            print(fundo, end='')
    print()
    sleep(tempo)
