# strings=["sun","bed","car"]
# n=1
strings=["abce","abcd","cdx"]
n=2
def solution(strings, n):
    answer = []
    temp_strings = {}
    for i, string in enumerate(strings):
        temp_strings[i] = [strings[i][n], string]
    values = sorted(temp_strings.values())
    for i in values:
        answer.append(i[1])
    return answer

print(solution(strings,n))


# 다른 풀이(sorted의 key 기능과, lambda의 활용)
'''
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])
'''


# 키가 겹치는 것 고려하지 못함(실패코드)
'''
temp_strings={}
for i, string in enumerate(strings):
    temp_strings[strings[i][n]] = string
print(temp_strings)
keys=sorted(list(temp_strings.keys()))
print(keys)
answer=[]
for key in keys:
    answer.append(temp_strings[key])
print(answer)
'''
