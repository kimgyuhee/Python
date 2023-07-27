"""
TypeError: cannot unpack non-iterable int object

​에러를 해석해보자면 "비문자적 정수형 객체 압축해제를 할 수 없음" 이라고 하는데요,

"""

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
            print(i, j)
            if i != 0 :
                for ii in range(i, 0, -1) :
                    print(ii)
                    board[ii][j] = board[ii-1][j]
                    for b in board :
                        print(b)
                    print()
                # board[i-1][j] = " "
                board[0][j] = " "
            else :
                board[i][j] = " "

        #for b in board :
        #    print(b)
        # print()

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
        print("===============================")
        answer += count
        if count == 0 :
            break

    return answer



print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) #14
print("-"*25)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) #15

i = 3
for ii in range(i, 0, -1) :
    print(ii)


    """
TypeError: cannot unpack non-iterable int object

​에러를 해석해보자면 "비문자적 정수형 객체 압축해제를 할 수 없음" 이라고 하는데요,

채점 결과
정확성: 81.8
합계: 81.8 / 100.0

"""

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
            print(i, j)
            if i != 0 :
                for ii in range(i, 0, -1) :
                    print(ii)
                    board[ii][j] = board[ii-1][j]
                    for b in board :
                        print(b)
                    print()
                # board[i-1][j] = " "
                board[0][j] = " "
            else :
                board[i][j] = " "

        #for b in board :
        #    print(b)
        # print()

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
        print("===============================")
        answer += count
        if count == 0 :
            break

    return answer



print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) #14
print("-"*25)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) #15
print("-"*25)
solution(2, 4, ["baab", "baab"]) # 답 : 4
