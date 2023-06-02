"""
양의 정수 n이 매개변수로 주어집니다. 
n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 
return 하는 solution 함수를 작성해 주세요.

입출력 예
n   result
4	[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
5	[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
"""
"""
행렬
[0][0] [0][1] [0][2] [0][3] / [0][n] 오른쪽 (0, 1)
[1][3] [2][3] [3][3] / [n][3] 아래쪽 (1, 0)
[3][2] [3][1] [3][0] / [3][n] 왼쪽 (0, -1)
[2][0] [1][0] / [n][0] 위쪽 (-1, 0)
[1][1] [1][2] / [1][n]
[2][2] / 
[2][1] /
"""


def solution(n):
    answer = [[0]*n for i in range(n)]
    num = 0
    while num != n**2 :
        print(num+1)
        num+=1
    return answer


def solution(n):
    direction = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위쪽
    overnum = 0
    i, j = 0, 0
    num = 0
    answer = [[0]*n for i in range(n)]

    while num != n**2 :
        num+=1
        print(i, j, num)
        answer[i][j] = num
        print("방향을 바꾸나요?")
        if not((i>=0 and i<n) and (j>=0 and j<n)):
            print("방향 바꿔요 ~")
            overnum +=1
        else :
            print("안바꿔여!! X")
        print(num, answer)
        d = direction[overnum%4]
        i = i+d[0]
        j = j+d[1]
    
    return answer



def solution(n):
    direction = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위쪽
    overnum = 0
    i, j = 0, 0
    num = 0
    answer = [[0]*n for i in range(n)]

    while num != n**2 :
        d = direction[overnum%4]
        num+=1
        print(i, j, num)
        print("방향을 바꾸나요?")
        if not((i+d[0]>=0 and i+d[0]<n) and (j+d[1]>=0 and j+d[1]<n)):
            print("방향 바꿔요 ~")
            overnum +=1
        else :
            print("안바꿔여!! X")
            answer[i][j] = num
            i = i+d[0]
            j = j+d[1]
        print(num, answer, d)
    return answer


def solution(n):
    direction = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위쪽
    overnum = 0
    i, j = 0, 0
    num = 0
    answer = [[0]*n for i in range(n)]

    while num != n**2 :
        num+=1
        print(i, j, num)
        print("방향을 바꾸나요?")
        if not((i>=0 and i<n) and (j>=0 and j<n)):
            print("방향 바꿔요 ~")
            i = i-d[0]
            j = j-d[1]
            print(i, j, num)
            overnum +=1
            d = direction[overnum%4]
            i = i+d[0]
            j = j+d[1]
            print(i, j, num)
            answer[i][j] = num
            continue
        else :
            print("안바꿔여!! X")
            answer[i][j] = num
            d = direction[overnum%4]
            i = i+d[0]
            j = j+d[1]
        print(num, answer, d)
    return answer


def solution(n):
    direction = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위쪽
    overnum = 0
    i, j = 0, 0
    num = 0
    answer = [[0]*n for i in range(n)]

    while num != n**2 :
        print(i, j, num)
        print("방향을 바꾸나요?")
        if not((i>=0 and i<n) and (j>=0 and j<n)) or answer[i][j] != 0:
            print("방향 바꿔요 ~")
            i = i-d[0]
            j = j-d[1]
            print(i, j, num)
            overnum +=1
            d = direction[overnum%4]
            i = i+d[0]
            j = j+d[1]
            print(i, j, num)
            continue
        else :
            num+=1
            print("안바꿔여!! X")
            answer[i][j] = num
            d = direction[overnum%4]
            i = i+d[0]
            j = j+d[1]
        print(num, answer, d)
    return answer



def solution(n):
    direction = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위쪽
    overnum = 0
    i, j = 0, 0
    num = 0
    answer = [[0]*n for i in range(n)]

    while num != n**2 :
        if not((i>=0 and i<n) and (j>=0 and j<n)) or answer[i][j] != 0:
            i, j = i-d[0], j-d[1]
            overnum +=1
            d = direction[overnum%4]
            i, j = i+d[0], j+d[1]
            continue
        else :
            num+=1
            answer[i][j] = num
            d = direction[overnum%4]
            i = i+d[0]
            j = j+d[1]
    return answer


# 다른 사람 풀이 1
def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer

# 다른 사람 풀이 2
dx=(0,1,0,-1)
dy=(1,0,-1,0)

def solution(n):
    board=[[0]*n for i in range(n)]
    x,y=0,0
    board[0][0]=1
    now=2
    d=0
    while now<=n*n:
        nx,ny=x+dx[d],y+dy[d]
        if not (0<=nx<n and 0<=ny<n) or board[nx][ny]:
            d=(d+1)%4
            continue
        x,y=nx,ny
        board[x][y]=now
        now+=1
    return board

print(solution(4))
print(solution(5))
print(solution(1))

