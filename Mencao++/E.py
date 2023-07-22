def valorKg(G, D, R):

  valorGrama = R / G
  valorPorKg = valorGrama * 1000 / (100 - D)
  return valorPorKg

G, D, R = map(float, input().split())
resultado = valorKg(G, D, R)
print("{:.8f}".format(resultado*100))
