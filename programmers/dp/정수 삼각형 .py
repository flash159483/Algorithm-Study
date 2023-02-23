# 정수 삼각형
# Level 3

# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
#
# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

def solution(tri):
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] += tri[i - 1][j]
            elif i == j:
                tri[i][j] += tri[i - 1][j - 1]

            else:
                tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1])

    return max(tri[-1])