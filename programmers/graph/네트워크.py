# 네트워크
# level 3

# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.


def solution(n, computers):
    def find(n1):
        while n1 != par[n1]:
            n1 = par[n1]
            par[n1] = par[par[n1]]
        return n1

    def union(n1, n2, num):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return num
        if p1 > p2:
            par[p2] = p1
            num -= 1
        else:
            par[p1] = p2
            num -= 1
        return num

    tmp = n
    par = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                tmp = union(i, j, tmp)

    return tmp

