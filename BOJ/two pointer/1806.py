# 1806
# gold 4

# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

#Example
#Input                      Ouput
# 10 15
# 5 1 3 5 10 7 4 9 2 8      2

import sys

n, target = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

l, r = 0, 0
result = sys.maxsize
s = 0
while True:
    if s >= target:
        result = min(result, r - l)
        s -= nums[l]
        l += 1
    else:
        if r == n:
            break

        s += nums[r]
        r += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)
