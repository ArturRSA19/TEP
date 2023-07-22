N, M = map(int, input().split())

doces = list(map(int, input().split()))

maior_doce = doces[0]
menor_sobra = maior_doce % M

for doce in doces:
    sobra = doce % M
    if sobra < menor_sobra or (sobra == menor_sobra and doce > maior_doce):
        menor_sobra = sobra
        maior_doce = doce

print(maior_doce)