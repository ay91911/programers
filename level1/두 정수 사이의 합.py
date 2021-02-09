a=5
b=3

def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        answer += i
    return answer

print(solution(a,b))

# sum 함수 이용한 사례
'''
def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))
'''