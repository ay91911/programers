s="a234"
# s="1234"


def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdecimal():
        answer = True
    else:
        answer= False
    return answer

print(solution(s))



'''
# if문 없이 바로 True, False 출력

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

'''