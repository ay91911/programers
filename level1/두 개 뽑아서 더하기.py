numbers= [2,1,3,4,1]
result= [2,3,4,5,6,7]

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            if numbers[i]+j not in answer:
                answer.append((numbers[i]+j))
    answer.sort()
    return answer

print(solution(numbers))

"""
모든 풀이 중(참고)
1. set: 순서가 없고, 집합안에서는 unique한 값을 가짐
   sorted: 오름차순 정렬 내장함수
   sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드"​​이며 리스트 원본값을 직접 수정합니다.
   sorted 함수는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환합니다.
   
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer))) =>[ answer, set 중복제거 후 list 리스트화 sorted 오름차순정렬 ]
    
2. combinations => 하나의 리스트에서 모든 조합을 계산해야 할 때

from itertools import combinations
def solution(numbers):
    numb = combinations(numbers, 2)
    result = set()
    for i in numb:
        result.add(i[0] + i[1])

    result = list(result)
    result.sort()
    answer = result
    return answer
 
"""

