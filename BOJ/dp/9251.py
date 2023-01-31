# 9251
# gold 5

# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
#
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
#Example
#Input                  Output
#ACAYKP                 4
#CAPCAK


word1 = input()
word2 = input()

n, m = len(word1), len(word2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)

print(dp[n][m])
