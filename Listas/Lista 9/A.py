def result(x, y):
    for i in range(y+1):
        if (x-i) % 500 == 0:
            return 'Yes'
    return 'No'

N = int(input()) #Qtd de yens que devem ser pagos
A = int(input()) #Qtd de yens que valem 1 yen

print(result(N, A))