def testePrimo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def proxPrimo(num):
    while True:
        if testePrimo(num): #Se for primo, retorna o número
            return num
        num += 1

x = int(input())

print(proxPrimo(x))

