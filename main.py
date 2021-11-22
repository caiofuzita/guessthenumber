import random

def jogo(a, b):
    contador = 0
    tentativa = None
    x = random.randrange(a, b)
    while tentativa != x:
        tentativa = int(input('Digite a sua tentativa: '))
        if tentativa < x:
            print('O valor digitado é menor')
            contador = contador + 1
        elif tentativa > x:
            print('O valor digitado é maior')
            contador = contador + 1
        else:
            contador = contador + 1
            print('Você ganhou!')
            print(f'Número de tentativas: {contador}')
            break

print('Guess the number!\n')
dificuldade = int(input('Digite a dificuldade desejada.\n1. Facil (0 a 100)\n2.Médio (0 a 500)\n3.Dificil (0 a 1000)\n'))

if dificuldade == 1:
    jogo(0, 101)
elif dificuldade == 2:
    jogo(0, 501)
elif dificuldade == 3:
    jogo(0, 1001)

