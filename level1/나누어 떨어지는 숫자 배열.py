arr=[5,9,7,10]
divisor=5

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer

print(solution(arr, divisor))