li = lambda :list(map(int,input().split()))

N,M = map(int,input().split())
 
f = [[0]*N for i in range(N)]
for _ in range(M):
    A = li()
    for a,b in zip(A,A[1:]):
        f[a-1][b-1] = 1
        f[b-1][a-1] = 1
 
res = 0
for i in range(N):
    for j in range(i+1,N):
        if f[i][j] == 0:
            res += 1
 
print(res)