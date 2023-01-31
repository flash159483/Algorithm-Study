# 11057
# silver 1

# 오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.
#
# 예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.
#
# 수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.
#Example
#Input                  Output
#1                      10


n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(10):
        if i == 1:
            dp[1][j] = 1
        else:
            dp[i][1] = 1


for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[n])%10007)
