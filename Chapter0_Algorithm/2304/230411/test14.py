"""
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 
위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

지뢰는 2차원 배열 board에 1로 표시되어 있고 
board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 
안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

"""
def solution(board):
    answer = 0
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            print(board[i][j], end= " ")
            if i == 0 :
                if j == 0:
                    if board[i][j+1] == 1 or board[i+1][j+1] == 1 or board[i+1][j] :
                        continue
                elif j == len(board[i])-1 :
                    if board[i][j+1] == 1 or board[i-1][j+1] == 1 or board[i-1][j] :
                        continue
                else :
                    if board[i][j+1] == 1 or board[i+1][j+1] == 1 or board[i+1][j] or board[i][j-1] == 1 or board[i-1][j-1] == 1:
                        continue
                answer +=1

            print()
    return answer
            

# 다른사람 풀이 
def solution(board):
    # 최초 모든 구역을 안전구역이라고 가정
    # (행의 수) * (열의 수)
    answer = len(board) * len(board[0])

    # [[각 열에 대한 원소] 각 행에 대한 원소]
    # _는 통상적으로 별 의미 없고 무시하는 변수로 사용
    # 문제에서 0은 안전지역, 1은 위험지역
    safe = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    def is_in_board(row, col):
        # board안에 있을 행의 조건: 0 <= row < len(board)
        # 열의 조건: 0 <= col < len(board[0])
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    # 변수명 
    # 행: r
    # 열: c
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                # 행에 대한 변화량: dr
                # 열에 대한 변화량: dc
                for dr in range(-1, 2):
                    nr = r + dr
                    for dc in range(-1, 2):
                        # 지뢰 주변의 구역 + 지뢰 구역에 대한 위치
                        # 행: nr, 열: nc
                        nc = c + dc

                        # (nr, nc)가 board안에 있는지 여부 확인
                        if is_in_board(nr, nc):
                            # 위험지역 카운트(최초 전체를 안전지역이라고 가정했으므로 1씩 빼기)
                            # xor 연산 이용
                            # 1. safe[nr][nc]가 1인 경우(이전에 위험지역으로 설정한 경우) 뺄 필요 없음
                            #    따라서 1 -> 0으로 계산
                            # 2. safe[nr][nc]가 0인 경우(이전에 위험지역으로 설정하지 않은 경우) 위험지역 카운트
                            #    따라서 0 -> 1로 계산
                            answer -= safe[nr][nc] ^ 1
                            # or 연산으로 위험지역 설정(safe[nr][nc]가 기존에 1이든 0이든 값은 1)
                            safe[nr][nc] |= 1

    return answer




def solution(board):
    answer = len(board) * len(board[0])
    safe = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    def is_in_board(row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                for dr in range(-1, 2):
                    nr = r + dr
                    for dc in range(-1, 2):
                        nc = c + dc

                        if is_in_board(nr, nc):
                            answer -= safe[nr][nc] ^ 1
                            safe[nr][nc] |= 1

    return answer

# 다른사람 풀이
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)


# 다른사람 풀이
def get_arounds(x, y, max_length):
    print(x, y, max_length)
    arounds = []

    for m in (-1, 0, 1):
        for n in (-1, 0, 1):
            loc = x+m, y+n
            if 0 <= loc[0] < max_length and 0 <= loc[1] < max_length:
                arounds.append(loc)

    print(arounds)
    return arounds


def solution(board):
    mines = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                mines.append((i,j))
    for x, y in mines:
        arounds = get_arounds(x, y, n)
        for a, b in arounds:
            board[a][b] = 1

    return sum(row.count(0) for row in board)

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))