checkBlockIdx = [(0, 1), (1, 0), (1, 1)]

def find2x2Block(i, j, board, removeBlockIdx) :
    value = board[i][j] # checkBlockidx (0, 0)

    if value == " " :
        return []
    
    result = True

    for ci, cj in checkBlockIdx :
        if value != board[i+ci][j+cj] :
            result = False
            break

    if result :
        if (i, j) not in removeBlockIdx :
            removeBlockIdx.append((i, j))
        for ci, cj in checkBlockIdx :
            if (i+ci, j+cj) not in removeBlockIdx :
                removeBlockIdx.append((i+ci, j+cj))

    return removeBlockIdx


def removeBlock(removeBlockIdx, board) :
    count = 0
    for i, j in removeBlockIdx :
        if board[i][j] != " " :
            count +=1
            if i != 0 :
                for ii in range(i, 0, -1) :
                    board[ii][j] = board[ii-1][j]
                board[0][j] = " "
            else :
                board[i][j] = " "
    return count

def solution(m, n, board):
    answer = 0
    boards = []

    for b in board :
        boards.append(list(b))

    while True :
        removeBlockIdx = []
        for i in range(m-1) :
            for j in range(n-1) :
                removeBlockIdx = find2x2Block(i, j, boards, removeBlockIdx)
                if len(removeBlockIdx) == 0 :
                    continue
        
        count = removeBlock(removeBlockIdx, boards)
        answer += count
        if count == 0 :
            break

    for b in boards :
        print(b)

    return answer



print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) #14
print("-"*25)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) #15
print("-"*25)
print(solution(2, 4, ["baab", "baab"])) # 답 : 4
print("-"*25)
print(solution(2, 4, ["aaaa", "aaaa"])) # 답 : 8
print("-"*25)
print(solution(2,2,["AA", "AA"]))
print("-"*25)
print(solution(2,2, ["AA", "AB"]))
print("-"*25)
print(solution(3,2, ["AA", "AA", "AB"]))
print("-"*25)
print(solution(4,2, ["CC", "AA", "AA", "CC"]) )
print("-"*25)
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"]))

