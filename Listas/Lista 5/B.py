x,y,z = map(int, input().split())
aux = 0

for i in range(x, y+1):
    if (((y-i) % z) == 0):
        aux += 1

print(aux)