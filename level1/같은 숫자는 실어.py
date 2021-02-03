arr=[1,1,3,3,0,1,1]
# arr=[4,4,4,3,3]

for i in range(len(arr)-1):
    if i<len(arr)-1:
        while arr[i]==arr[i+1]:
            if i+1 != len(arr)-1:
                arr.remove(arr[i])
            else:
                break
if arr[-2]==arr[-1]:
    arr.remove(arr[-2])

print(arr)




def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer