# s="abcde"
s="qwer"

if len(s)%2 == 0:
    answer=s[len(s)//2-1:len(s)//2+1]
else :
    answer=s[len(s)//2]

print(answer)

# 함수화
def solution(s):
    if len(s) % 2 == 0:
        answer = s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        answer = s[len(s) // 2]
    return answer

print(solution(s))