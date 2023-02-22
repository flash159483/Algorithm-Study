# 카펫
# Level 2

# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
#
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(brown, yellow):
    total = brown + yellow
    w, h = 1, 1
    prev = [w, h]
    while True:
        if w * h == total:
            if 2 * w + 2 * h - 4 == brown:
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]
            w = prev[0]
            h += 1
        elif w * h > total:
            w = prev[0]
            h += 1
        else:
            w += 1
