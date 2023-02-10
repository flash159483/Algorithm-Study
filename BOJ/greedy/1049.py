# 1049
# silver 4

# Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다.
# 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
#
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때,
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.


# Example
# input         output
# 4 2           12
# 12 3
# 15 4

n, m = map(int, input().split())
six, one = [], []
result = 0
for i in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)

s, o = min(six), min(one)

if s <= o * 6:
    result = s * (n // 6) + o * (n % 6)
    if s  < o * (n % 6):
        result = s * (n // 6 + 1)
else:
    result = o * n

print(result)
