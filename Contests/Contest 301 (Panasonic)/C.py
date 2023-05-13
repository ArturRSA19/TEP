S = input()
T = input()
 
S_at = [0 for i in range(8)]
T_at = [0 for i in range(8)]

atcoder = list("atcoder")
 
d = {}
now = 0
for i in atcoder:
  d[i] = now
  now += 1
 
S_not = 0
T_not = 0
set_atcoder = set(atcoder)
for i in range(len(S)):
  if S[i] not in set_atcoder and S[i] != "@":
    S_not += 1
  if T[i] not in set_atcoder and T[i] != "@":
    T_not += 1
if S_not != T_not:
  print("No")
  exit()
for i in range(len(S)):
  if S[i] == "@":
    S_at[7] += 1
  if T[i] == "@":
    T_at[7] += 1
  if S[i] in set_atcoder:
    S_at[d[S[i]]] += 1
  if T[i] in set_atcoder:
    T_at[d[T[i]]] += 1
for i in range(7):
  if S_at[i] == T_at[i]:
    continue
  elif S_at[i] > T_at[i]:
    if T_at[i] + T_at[7] >= S_at[i]:
      T_at[7] -= (S_at[i] - T_at[i])
    else:
      print("No")
      exit()
  else:
    if S_at[i] + S_at[7] >= T_at[i]:
      S_at[7] -= (T_at[i] - S_at[i])
    else:
      print("No")
      exit()
print("Yes")