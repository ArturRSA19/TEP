import math

def ataque(x, y):
    minimo = math.ceil(x//y)
    if (x%y != 0):
        minimo += 1
    return minimo

A, B = map(int, input().split())

print(ataque(A,B))


