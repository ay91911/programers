# answers=[1,2,3,4,5]
answers=[1,3,2,4,2]

#enumerate 익히기! 인덱스와 값을 반복문 사용하여 호출할 시 사용

def solution(answers):
    answer = []
    answer_num = []
    count01 = 0
    count02 = 0
    count03 = 0

    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            count01+=1
        if answers[i] == second[i%len(second)]:
            count02+=1
        if answers[i] == third[i%len(third)]:
            count03+=1

    answer_num = [count01, count02, count03]

    for person, score in enumerate(answer_num):
        if score == max(answer_num):
            answer.append(person+1)

    return answer


print(solution(answers))


# answers=[1,2,3,4,5]
# # answers=[1,3,2,4,2]
# # 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# # 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# # 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# first=[]
# second=[]
# third=[]
#
# #첫번째 수포자 정답지
# for i in range(1,len(answers)+1):
#     if i%5!=0:
#         j=i%5
#     else:
#         j=5
#     first.append(j)
#
# print(first)
#
# #두번째 수포자 정답지
# .. 이런식으로 접근할 시 너무 비효율적임..


