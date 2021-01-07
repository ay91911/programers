# board = [[0,2,0],[1,2,0],[2,2,1]]
# moves = [1,2,2,2,1,3]
# board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 1, 4]
board= [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves= [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]

def solution(board, moves):
    basket = []
    answer = 0
    i =0

    for move in moves:
        for j in range(0, len(board)):
            if board[j][move - 1] == 0:
                continue
            else:
                basket.append(board[j][move - 1])
                board[j][move - 1] = 0
                break
    # print(basket)

    while True:
        if basket[i] != basket[i + 1]:
            i+=1
            if i ==len(basket)-1:
                break
            else:
                continue
        else:
            del basket[i:i + 2]
            answer += 2
            i=0
            # print(basket)
            # print(answer)
            if len(basket)<=1 :
                break

    return answer


print(solution(board,moves))