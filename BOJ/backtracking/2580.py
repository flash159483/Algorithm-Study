# 2580
# Gold 4

# 스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.
#
#
#
# 나머지 빈 칸을 채우는 방식은 다음과 같다.
#
# 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.
#
#
#
# 또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.
#
#
#
# 이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.
#
#
#
# 게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

# Example
# Input:
# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0

# output
# 1 3 5 4 6 9 2 7 8
# 7 8 2 1 3 5 6 4 9
# 4 6 9 2 7 8 1 3 5
# 3 2 1 5 4 6 8 9 7
# 8 7 4 9 1 3 5 2 6
# 5 9 6 8 2 7 4 1 3
# 9 1 7 6 5 2 3 8 4
# 6 4 3 7 8 1 9 5 2
# 2 5 8 3 9 4 7 6 1

import sys

input = sys.stdin.readline


def threebythree(x, y):
    dx, dy = x // 3 * 3, y // 3 * 3
    left = list(range(1, 10))
    for i in range(dx, dx + 3):
        for j in range(dy, dy + 3):
            if table[i][j] in left:
                left.remove(table[i][j])
    return left


def checkline(x, y, a):
    for i in range(9):
        if table[x][i] == a:
            return False
    for i in range(9):
        if table[i][y] == a:
            return False
    return True


def dfs(cur):
    if cur == len(space):
        for i in table:
            print(*i)
        exit()

    x, y = space[cur]
    for i in threebythree(x, y):
        if checkline(x, y, i):
            table[x][y] = i
            dfs(cur + 1)
            table[x][y] = 0
    return


space = []
table = []
for i in range(9):
    table.append(list(map(int, input().split())))
    for j in range(9):
        if table[i][j] == 0:
            space.append((i, j))

dfs(0)

