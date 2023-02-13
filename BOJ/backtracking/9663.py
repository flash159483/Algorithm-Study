# 9663
# gold 4

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# Example
# Input         Output
# 8             92

n = int(input())

place = [0] * n
result = 0


def check(cur):
    for i in range(cur):
        # check if the queen is already in that col or in the same diagonal
        if place[i] == place[cur] or abs(place[i] - place[cur]) == abs(i - cur):
            return False
    return True


def dfs(cur):
    global result
    if cur == n:
        result += 1
        return
    for i in range(n):
        # does not have to check same row since the queen can travel through same row
        place[cur] = i
        if check(cur):
            dfs(cur+1)


dfs(0)
print(result)