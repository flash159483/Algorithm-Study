# 2170
# gold 5

# 매우 큰 도화지에 자를 대고 선을 그으려고 한다. 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다. 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다고 하자.
#
# 이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성하시오. 선이 여러 번 그려진 곳은 한 번씩만 계산한다.


# Example:
# input         Output
# 4             5
# 1 3
# 2 5
# 3 5
# 6 7

import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

start, end = arr[0][0], arr[0][1]
result = 0
for i in range(1, n):
    if arr[i][0] < end:
        end = max(end, arr[i][1])
    else:
        result += (end - start)
        start = arr[i][0]
        end = arr[i][1]

result += (end - start)
print(result)