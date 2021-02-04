# arr=[1,1,3,3,0,1,1]
arr=[4,4,4,3,3]

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0:
            answer.append(arr[i])
        else:
            if arr[i]!=arr[i-1]:
                answer.append(arr[i])
    return answer


# 슬라이싱은 인덱스 초과해도 에러가 뜨지 않는다!
'''
def no_continuous(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer
'''

# solution2,3는 시간초과......
'''
def solution2(arr):
    answer = []

    for i in range(len(arr)):
        if [arr[i]]==answer[-1:]:continue
        j=1
        while arr[i]==arr[i+j:]:
            j+=1
        if j>1 and answer[-1:]!=arr[i+j-1]:
            answer.append(arr[i+j-1])
        elif answer[-1:]!=arr[i]:
            answer.append(arr[i])
    return answer
'''
'''
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i<len(arr)-1:
            j=1
            while arr[i]==arr[i+j]:
                j+=1
                if i+j > len(arr)-1: break
            if j>1 :
                if len(answer)==0:
                    answer.append(arr[i+j-1])
                else:
                    if arr[i+j-1]!=answer[-1]:
                        answer.append(arr[i + j - 1])
            elif arr[i]!=arr[i+1] and arr[i+1]!=arr[i+2]:
                answer.append(arr[i+1])
    return answer

'''



print(solution(arr))