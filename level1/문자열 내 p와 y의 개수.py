s="pPoooyY"
# s="Pyy"


def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        answer = True
    else:
        answer = False
    return answer

print(solution(s))