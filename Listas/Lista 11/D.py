N = int(input())
S = list(input())

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(S)):
  aux = alfabeto.find(S[i]) #Guarda o índice 'i' da letra para manipulação
  if aux+N > 25:
    aux = aux+N-26
  else:
    aux = aux+N
  S[i] = alfabeto[aux] #Substitui a letra modificada pela original na string 'S'
print(''.join(S))

