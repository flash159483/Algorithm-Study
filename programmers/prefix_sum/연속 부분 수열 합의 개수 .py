# 연속 부분 수열 합의 개수
# Level 2

# 철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다.
# 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.


def solution(elements):
    ans = set([sum(elements)])

    for w in range(1, len(elements)):
        total = sum(elements[:w])
        start, end = 0, w
        for _ in range(len(elements)):
            total += elements[end] - elements[start]
            start, end = start + 1, (end + 1) % len(elements)
            ans.add(total)

    return len(ans)