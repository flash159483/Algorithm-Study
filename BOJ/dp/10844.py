#10844
# silver 1

# 45656이란 수를 보자.
#
# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
#
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

#Example
#Input              Output
#1                  9

n = int(input())
dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)