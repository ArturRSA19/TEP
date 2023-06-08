n = int(input())

lista = []

elementos = input()
valores = elementos.split()

for valor in valores:
    lista.append(int(valor))

soma = 0

for num in lista:
    soma+=num

resultado = soma/n

print(f'{resultado:.12f}')