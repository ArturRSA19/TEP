import math

t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    aux = y - x # Valor necessário para chegar de x até y
    resultado = math.ceil(abs(aux) / 10) # Número mínimo de movimentos necessários para alcançar o múltiplo de 10 mais próximo

    if resultado > 0:
        x += resultado * 10

    x += aux

    print(resultado)
    #Resetando valores para reinicar o loop com outras entradas, caso existam
    aux = 0
    resultado = 0


