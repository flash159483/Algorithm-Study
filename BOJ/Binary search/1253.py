# 1253
# gold 4

# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
#
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
#
# 수의 위치가 다르면 값이 같아도 다른 수이다.

#Example
#Input                  Output
# 10                      8
# 1 2 3 4 5 6 7 8 9 10

import sys


n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = 0
for i in range(len(arr)):
    tmp = arr[:i] + arr[i + 1:]
    l, r = 0, len(tmp)-1
    while l < r:
        addup = tmp[l] + tmp[r]
        if addup < arr[i]:
            l += 1
        elif addup > arr[i]:
            r -= 1
        else:
            result += 1
            break

print(result)
