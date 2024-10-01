import random
a = int(input('Digite o número inicial da sua sequência:'))
b = int(input('Digite o número final de sua sequência:'))
elemento_aleatorio = random.randint(a,b)
x = int(input(f"Digite um número de {a} - {b}:"))
while (x != elemento_aleatorio):
    x = int(input())
    if x > elemento_aleatorio:
        print('Seu número é maior q o número escolhido!')
    elif x < elemento_aleatorio:
        print('Seu número é menor que p número escolhido!')
    else:
        print('Parabéns!! Você acertou o número escolhido!')
    

