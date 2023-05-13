N = int(input())
a = input().split()

A = [int(x) for x in a]
B= []

for i in range(len(A)):
    B.append(A[i])
    if i < len(A) - 1:
        diff = A[i+1] - A[i]

        step = 1 if diff >= 0 else -1
        for j in range(1, abs(diff)):
            B.append(A[i] + j * step)

print(' '.join(map(str, B)))