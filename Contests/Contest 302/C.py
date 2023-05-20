def validaDuplas(p1, p2): #Valida a quantidade de letras diferentes que as duplas possuem
    count = 0
    for letra1, letra2 in zip(p1, p2):
        if letra1 != letra2:
            count += 1
    return count

def validaLista(lista): #Valida se a lista atende as condições
    n = len(lista)
    aux = 0

    for i in range(n):
        for j in range(i + 1, n):
            if validaDuplas(lista[i], lista[j]) == 1: #Valida a quantidade de duplas que satisfazem a condição na lista
                aux += 1

    if aux >= n - 1: #Valida se a quantidade de duplas validadas supera ou igual o número de entradas na lista s
        return "Yes"
    else:
        return "No"

n, m = map(int, input().split())

s = []

for i in range (n):
    s.append(input())

possibilidade = validaLista(s)

print(possibilidade)
