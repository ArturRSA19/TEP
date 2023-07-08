A, B = map(int, input().split())

linha1 = [1, 2, 3]
linha2 = [4, 5, 6]
linha3 = [7, 8, 9]

aux = abs(A-B)
print(aux)

if A in linha3 and B in linha3:
    if(aux == 1):
        print('yes')