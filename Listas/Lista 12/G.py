n, d = map(int, input().split())

numMinMovimentos = 0
nAnterior = 0

elementos = list(map(int, input().split()))

for i in range(n):
    nAtual = elementos[i]
    
    if nAnterior >= nAtual:
        passosParaAdd = (nAnterior - nAtual + 1) // d
        passosParaAdd += 0 if (nAnterior - nAtual + 1) % d == 0 else 1

        nAtual = nAtual + passosParaAdd * d
        numMinMovimentos += passosParaAdd
    
    nAnterior = nAtual

print(numMinMovimentos)
