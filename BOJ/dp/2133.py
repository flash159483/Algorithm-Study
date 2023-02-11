# 2133
# gold 4

# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

# Example
# Input             Output
# 2                 3

n = int(input())

dp = [0]*31
dp[0] = 1

for i in range(2, n+1, 2):
    dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2


print(dp[n])