# 이모티콘 할인행사
# level 2

# 카카오톡에서는 이모티콘을 무제한으로 사용할 수 있는 이모티콘 플러스 서비스 가입자 수를 늘리려고 합니다.
# 이를 위해 카카오톡에서는 이모티콘 할인 행사를 하는데, 목표는 다음과 같습니다.
#
# 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 이모티콘 판매액을 최대한 늘리는 것.
# 1번 목표가 우선이며, 2번 목표가 그 다음입니다.
#
# 이모티콘 할인 행사는 다음과 같은 방식으로 진행됩니다.
#
# n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매합니다.
# 이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
# 카카오톡 사용자들은 다음과 같은 기준을 따라 이모티콘을 사거나, 이모티콘 플러스 서비스에 가입합니다.
#
# 각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
# 각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다.


def solution(users, emoticons):
    discount = []

    def dfs(tmp, cnt):
        if len(tmp) == cnt:
            discount.append(tmp[:])
            return

        for i in (10, 20, 30, 40):
            tmp[cnt] += i
            dfs(tmp, cnt + 1)
            tmp[cnt] -= i

    dfs([0] * len(emoticons), 0)
    ans = [0, 0]
    for d in discount:
        sub = 0
        sale = [0] * len(users)
        for i in range(len(emoticons)):
            for j in range(len(users)):
                if users[j][0] <= d[i]:
                    sale[j] += emoticons[i] * (100 - d[i]) // 100

        for i, u in enumerate(users):
            if sale[i] >= u[1]:
                sub += 1
                sale[i] = 0

        if ans[0] <= sub:
            if sub == ans[0]:
                ans[1] = max(ans[1], sum(sale))
            else:
                ans[1] = sum(sale)
            ans[0] = sub

    return ans



