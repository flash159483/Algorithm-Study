# 개인정보 수집 유효기간
# level 1

# 고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.
#
# 예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
# 당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.


def daysdif(today, days):
    y1, m1, d1 = map(int, today.split('.'))
    y2, m2, d2 = map(int, days.split('.'))
    month = day = 0
    if y1 - y2 != 0:
        month += (y1 - y2) * 12
    month += m1 - m2
    if d1 - d2 < 0:
        month -= 1
        day = (28 - d2) + d1
    day = d1 - d2
    return (month, day)


def solution(today, terms, privacies):
    term = {}
    for t in terms:
        a, b = t.split()
        term[a] = int(b)

    result = []
    for i, p in enumerate(privacies):
        d, t = p.split()
        m, day = daysdif(today, d)
        if m >= term[t]:
            result.append(i + 1)

    return result