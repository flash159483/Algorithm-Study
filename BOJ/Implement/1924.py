# 1924
# Bronze 1

# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
#Example
#Input                  Output
#1 1                    MON

month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

m, d = map(int, input().split())

total = d

for i in range(1, m):
    total += month[i]

tmp = total % 7

if tmp == 1:
    print('MON')
elif tmp == 2:
    print('TUE')
elif tmp == 3:
    print('WED')
elif tmp == 4:
    print('THU')
elif tmp == 5:
    print('FRI')
elif tmp == 6:
    print('SAT')
else:
    print('SUN')