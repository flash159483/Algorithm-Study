# 9095
# Silver 3

# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
#
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.


# Example:
# Input             output
# 3                 7
# 4                 44
# 7                 274
# 10

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    dp = [0] * 11

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[num])