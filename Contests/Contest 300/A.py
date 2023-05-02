N, A, B = input().split()
N, A, B = [int(N), int(A), int(B)]
C = list(map(int, input().split()))

for i in len(C):
    if(C[i] == (A+B)):
        print(i+1)
