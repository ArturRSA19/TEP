n, m = map(int, input().split())

if m >= n * (n + 1) // 2:
    m %= n * (n + 1) // 2

i = 1
while m >= i:
    m -= i
    i += 1

print(m)
