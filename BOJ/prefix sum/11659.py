# 11659
# silver 3

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# Example
# Input                     Output
# 5 3                       12
# 5 4 3 2 1                 9
# 1 3                       1
# 2 4
# 5 5

import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(itertools.accumulate(arr))

for _ in range(m):
    a, b = map(int, input().split())
    if a != 1:
        print(arr[b-1] - arr[a-2])
    else:
        print(arr[b-1])