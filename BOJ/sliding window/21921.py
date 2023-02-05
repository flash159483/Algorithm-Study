# 21921
# silver 3

# 찬솔이는 블로그를 시작한 지 벌써
# $N$일이 지났다.
#
# 요즘 바빠서 관리를 못 했다가 방문 기록을 봤더니 벌써 누적 방문 수가 6만을 넘었다.
#
#
#
# 찬솔이는
# $X$일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.
#
# 찬솔이를 대신해서
# $X$일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.


# Example
#input              output
# 5 2               7
# 1 4 2 5 1         1

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
count = 0
addup = sum(arr[:m-1])
for i in range(m-1, n):
    addup += arr[i]
    if addup > result:
        count = 0
        count += 1
        result = addup
    elif addup == result:
        count += 1
    addup -= arr[i-m+1]

if result != 0:
    print(result)
    print(count)
else:
    print('SAD')