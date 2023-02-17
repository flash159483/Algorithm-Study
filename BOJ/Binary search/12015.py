# 12015
# Gold 2

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# Example
# Input                     Output
# 6
# 10 20 10 30 20 50         4


import bisect
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]
for num in arr:
    if result[-1] < num:
        result.append(num)
    else:
        index = bisect.bisect_left(result, num)
        result[index] = num

print(len(result))