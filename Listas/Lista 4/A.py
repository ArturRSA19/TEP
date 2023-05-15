x = int(input())
aux = 1

for i in range(2, x+1):
    y = i
    while y <= x:
        y *= i
        if y <= x:
            aux = max(aux, y)

print(aux)