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