def contFatoresPrimos(n):
    fatores = set()  # Conjunto para armazenar os fatores primos únicos
    i = 2  # Começamos com o menor número primo

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fatores.add(i)

    if n > 1:
        fatores.add(n)

    return len(fatores)


# Teste a função
while True:
    num = int(input())
    if(num != 0):
        print(f'{num} : {contFatoresPrimos(num)}')
    if(num == 0):
        break
