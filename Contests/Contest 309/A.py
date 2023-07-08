def testeLinha(lista, x, y):
    if x in lista and y in lista:
        diferenca = abs(x-y)
        if(diferenca != 1):
            return 'nao'
        else:
            return 'sim'

A, B = map(int, input().split())

linha1 = [1, 2, 3]
linha2 = [4, 5, 6]
linha3 = [7, 8, 9]

resultado1 = testeLinha(linha1, A, B)
resultado2 = testeLinha(linha2, A, B)
resultado3 = testeLinha(linha3, A, B)

if(resultado1 == 'sim' or resultado2 == 'sim' or resultado3 == 'sim'):
    print('Yes')
else:    
    print('No')


        


