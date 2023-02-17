# 2230
# Gold 5

# N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.
#
# 예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.

# Example
# Input                     Output
# 3 3                       4
# 1
# 5
# 3

import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = sys.maxsize
for i in range(n):
    index = bisect.bisect_left(arr, arr[i]+m)

    if index < n:
        result = min(result, arr[index] - arr[i])

print(result)
