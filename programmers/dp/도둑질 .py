# 도둑질
# level 4

# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.
#
# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
#
# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.


def solution(money):
    dp = [0] * len(money)

    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    result = max(dp)
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    result = max(result, max(dp))

    return result