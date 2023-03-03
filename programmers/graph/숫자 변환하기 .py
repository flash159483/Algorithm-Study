# 숫자 변환하기
# Level 2

# 자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.
#
# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.
# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.


import collections


def solution(x, y, n):
    q = collections.deque([x])
    visited = [-1] * (y + 1)
    visited[x] = 0
    while q:
        cur = q.popleft()
        if cur == y:
            return visited[y]
        for nx in (cur + n, cur * 2, cur * 3):
            if nx <= y and visited[nx] == -1:
                visited[nx] = visited[cur] + 1
                q.append(nx)

    return -1
