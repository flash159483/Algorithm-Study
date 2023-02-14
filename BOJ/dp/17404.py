# 17404
# gold 4

# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
#
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
#
# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

# Example
# Input                 Output
# 3                     110
# 26 40 83
# 49 60 57
# 13 89 99

import sys

input = sys.stdin.readline

n = int(input())
price = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize

for a in range(3):
    dp = [[sys.maxsize] * 3 for _ in range(n)]
    dp[0][a] = price[0][a]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + price[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + price[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + price[i][2]
    for i in range(3):
        if a != i:
            result = min(result, dp[n-1][i])

print(result)