def ordenaMesa():
    N = int(input())
    listaPessoas = []

    for i in range(N):
        nome, idade = input().split()
        listaPessoas.append((nome, int(idade)))

    iMaisNovo = listaPessoas.index(min(listaPessoas, key=lambda x: x[1]))
    aux = [listaPessoas[(iMaisNovo + i) % N][0] for i in range(N)]

    for i in range(N):
        print(aux[i])

ordenaMesa()
