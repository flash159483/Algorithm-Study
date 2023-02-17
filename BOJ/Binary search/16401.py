# 16401
# silver 2

# 명절이 되면, 홍익이 집에는 조카들이 놀러 온다. 떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.
#
# 조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.
#
# 그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.
#
# M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.
#
# 단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.

# Example
# Input                     Output
# 3 10                      8
# 1 2 3 4 5 6 7 8 9 10

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, max(arr)
result = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for i in range(m):
        if mid <= arr[i]:
            cnt += (arr[i] // mid)
    if cnt >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)