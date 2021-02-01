array = [1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer=[]

for i in range (len(commands)):
    temp_array=array[commands[i][0] - 1:commands[i][1]]
    temp_array.sort()
    answer.append(temp_array[commands[i][2]-1])

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp_array = array[commands[i][0] - 1:commands[i][1]]
        temp_array.sort()
        answer.append(temp_array[commands[i][2] - 1])
    return answer
'''
----------------------------------------
간단한 풀이법

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''