seoul =["Jane","Kim"]


def solution(seoul):
    answer = '김서방은 '+str(seoul.index("Kim"))+"에 있다"
    return answer

print(solution(seoul))

'''
# format 활용
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
    
# %d 사용
def solution(seoul):
    answer = ''
    return ('김서방은 %d에 있다' %seoul.index('Kim'))
'''



'''
def solution(seoul):
    answer = ''
    for index, s in enumerate(seoul):
        if(s=="Kim"): 
            answer+= "김서방은 " + str(index) + "에 있다"
    return answer
'''