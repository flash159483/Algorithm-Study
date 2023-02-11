# 11726
# Silver 3

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

# Example
# Input             Output
# 2                 2

num = int(input())

dp = [0, 1, 2]

for i in range(3, num+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[num]%10007)