"""
프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 
이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 
같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.
"""
def checkInxBlock(m,n, board) :
    idxs = []
    for i in range(m) :
        idx = []
        for j in range(n) :
            print(board[i][j], end=" ")
            idx.append([i, j])
        print()
        idxs.append(idx)
    return idxs

checkBlockIdx = [(0, 1), (1, 0), (1, 1)]
removeBlockIdx = []
def find2x2Block(i, j, board) :
    value = board[i][j] # checkBlockidx (0, 0)
    if value == " " :
        return False
    
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
    return result


def removeBlock(removeBlockIdx, board) :
    count = 0
    for i, j in removeBlockIdx :
        # print(board[i][j], i, j)
        # print(type(board[i][j]))
        if board[i][j] != " " :
            count +=1
            print(i, j)
            iii = 0
            if i != 0 :
                board[i][j] = board[i-1][j]    
                board[i-1][j] = " "
            else :
                board[i][j] = " "

        for b in board :
            print(b)
        print()
    return count

def solution(m, n, board):
    answer = 0
    boards = []

    for b in board :
        boards.append(list(b))

    while True :
        for i in range(m-1) :
            for j in range(n-1) :
                if not find2x2Block(i, j, boards) :
                    continue
    
        count = removeBlock(removeBlockIdx, boards)
        print("===============================")
        answer += count
        if count == 0 :
            break

    return answer

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) #14
print("-"*25)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) #15