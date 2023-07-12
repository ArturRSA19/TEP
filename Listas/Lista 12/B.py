frase = str(input())
aux = 0
for i in range(len(frase)):
    if frase[i] != frase[::-1][i]:
        aux += 1
print(aux//2)