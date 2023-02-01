# 1644
# gold 3

# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
#
# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
# 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
#
# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

#Example
#Input                      Ouput
# 20                        0

import sys


num = int(sys.stdin.readline().rstrip())
prime = []
arr = []
a = [False,False] + [True]*(num-1)
for i in range(2,num+1):
  if a[i]:
    prime.append(i)
    for j in range(2*i, num+1, i):
        a[j] = False

for i in range(num+1):
    if a[i]:
        arr.append(i)
l, r = 0, 1
result = 0

while l <= r <= len(arr):
    s = sum(arr[l:r])
    if s == num:
        result += 1
        r += 1
    elif s < num:
        r += 1
    else:
        l += 1

print(result)

