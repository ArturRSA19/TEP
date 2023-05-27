x, y, z = map(int, input().split())
s = input()

dp = [0, z]
for letra in s:
    if letra == 'a':
        dp = [min(dp[0] + x, dp[1] + z + x), min(dp[1] + y, dp[0] + z + y)]
    else:
        dp = [min(dp[0] + y, dp[1] + z + y), min(dp[1] + x, dp[0] + z + x)]

print(min(dp))
