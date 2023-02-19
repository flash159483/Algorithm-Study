# 1461
# gold 5

# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다.
# 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다.
# 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.


# Example:
# input                         Output
# 7 2                           131
# -37 2 -6 -39 -29 11 -28

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
pos, neg = [], []

for i in arr:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

neg.sort()
result = []
for i in range(len(neg)//m):
    result.append(abs(neg[i*m]))
if len(neg) % m > 0:
    result.append(abs(neg[len(neg) // m * m]))

pos.sort(reverse=True)
for i in range(len(pos)//m):
    result.append(pos[i*m])
if len(pos) % m > 0:
    result.append(pos[len(pos) // m * m])

long = max(result)
ans = (sum(result) - long) * 2 + long
print(ans)