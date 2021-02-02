import datetime

# 2016년 1월1일: 금요일

# 2016년 a월 b일
a=5
b=24

date=[31,29,31,30,31,30,31,31,30,31,30,31]

b=sum(date[:a-1])+b

if b%7==1:
    answer='FRI'
elif b%7==2:
    answer='SAT'
elif b%7==3:
    answer='SUN'
elif b%7==4:
    answer='MON'
elif b%7==5:
    answer='TUE'
elif b%7==6:
    answer='WED'
elif b%7==0:
    answer='THU'

print(answer)

# 함수화
def solution(a, b):
    b = sum(date[:a - 1]) + b

    if b % 7 == 1:
        answer = 'FRI'
    elif b % 7 == 2:
        answer = 'SAT'
    elif b % 7 == 3:
        answer = 'SUN'
    elif b % 7 == 4:
        answer = 'MON'
    elif b % 7 == 5:
        answer = 'TUE'
    elif b % 7 == 6:
        answer = 'WED'
    elif b % 7 == 0:
        answer = 'THU'

    return answer

'''datetime 함수의 활용

# 요일 list
day=['MON','TUE','WED','THU','FRI','SAT','SUN']

print(day[datetime.date(2016,a,b).weekday()])

def solution(a, b):
    answer = day[datetime.date(2016,a,b).weekday()]
    return answer

print(solution(a,b))

'''

