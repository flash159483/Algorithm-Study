# 1068
# gold 5

# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
#
# 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
#
# 예를 들어, 다음과 같은 트리가 있다고 하자.
#
# 현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.
#
# 이제 리프 노드의 개수는 1개이다.


# Example
# Input             Output
# 5                 2
# -1 0 0 1 1
# 2


import sys


def dfs(e):
    arr[e] = -2
    for i in range(n):
        if e == arr[i]:
            dfs(i)


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
erase = int(input())

dfs(erase)
result = 0

for i in range(n):
    if arr[i] != -2 and i not in arr:
        result += 1

print(result)
