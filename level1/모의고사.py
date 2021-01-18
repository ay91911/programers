from more_itertools import chain, repeat


answers=[1,2,3,4,5]
# answers=[1,3,2,4,2]
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
first=[]
second=[]
third=[]

#첫번째 수포자 정답지
for i in range(1,len(answers)+1):
    if i%5!=0:
        j=i%5
    else:
        j=5
    first.append(j)

print(first)

#두번째 수포자 정답지


def solution(answers):
    answer = []
    return answer