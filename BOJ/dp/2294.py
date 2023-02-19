# 2294
# Gold 5

# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
#
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
#

# Example:
# input             output
# 3 15              3
# 1
# 5
# 12

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [sys.maxsize] * (k+1)
dp[0] = 0

for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
