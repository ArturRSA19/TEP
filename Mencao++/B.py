def color_combo(base, pieces):

  bonus = 0
  if pieces > 3:
    bonus = 0.25

  if pieces > 7:
    bonus = 0.5

  pontuacao = base + (pieces - 3) * 100
  pontuacaoFinal = pontuacao + (pontuacao * bonus)

  if pontuacao== 1:
    return "1 ponto"
  else:
    return str(int(pontuacaoFinal)) + " pontos"


t = int(input())
for i in range(t):
  base, pieces = map(int, input().split())
  score = color_combo(base, pieces)
  print("Caso {}: {}".format(i + 1, score))
