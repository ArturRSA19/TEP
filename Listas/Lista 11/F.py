N = int(input())
aux = 0

lista = input().split()

lista = list(map(int, lista))

for num in lista:
    maior = max(lista)
    if(num < maior):
        aux+=(maior-num)

print(aux)