# 10986
# gold 3

# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
#
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

# Example
# Input                     Output
# 5 3                       7
# 1 2 3 1 2

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * m
prefix[0] = 1
tmp = 0
for i in range(n):
    tmp += arr[i]
    prefix[tmp % m] += 1
result = 0
for i in prefix:
    result += i * (i - 1) // 2

print(result)