
# participant= ["leo", "kiki", "eden"]
# completion= ["eden", "kiki"]
# participant=["marina", "josipa", "nikola", "vinko", "filipa"]
# completion= ["josipa", "filipa", "marina", "nikola"]
participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]


'''
collections.Counter() 함수 사용이 제일 효과적
'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(participant, completion))

'''
딕셔너리를 사용해야 효율성을 높일 수 있음.

def solution(participant, completion):
    answer = ''
    basket = {}
    for i in participant:
        if i not in basket:
            basket[i] = 0
        if i in basket:
            basket[i] = basket.get(i) + 1
    for j in completion:
        basket[j] = basket.get(j)-1
    for i in participant:
        if basket[i] == 1:
            answer = i
    return answer

print(solution(participant, completion))
'''

# 시간초과..
'''
def solution(participant, completion):
    answer = ''
    for i in completion:
        for j in participant:
            if i == j:
                participant.remove(j)
                break
    answer = participant[0]
    return answer

print(solution(participant,completion))
'''


