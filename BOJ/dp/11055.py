#11055
#silver 2

# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

#example
#input                              output
# 10                                113
# 1 100 2 50 60 3 5 6 7 8

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
for i in range(n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])


print(max(dp))
