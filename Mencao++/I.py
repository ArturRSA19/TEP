R, V = map(float, input().split())
I, J = map(float, input().split())

valorPoupanca = 0
aux = 0

while valorPoupanca < V:
    valorPoupanca += R
    valorPoupanca *= (1 + I / 100)
    V *= (1 - J / 100)
    aux += 1

    if aux > 52 * 70:
        break

if aux > 52 * 70:
    print(-1)
else:
    print(aux)
