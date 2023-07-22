def num_maneiras_roleta(n):
  
  if n == 1:
    return 1
  
  resultado = 1
  for i in range(1,n):
    resultado *= i

  return resultado

n = int(input())
print(num_maneiras_roleta(n))
