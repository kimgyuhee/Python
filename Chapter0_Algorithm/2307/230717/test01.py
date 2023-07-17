"""
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다.

명령어는 다음과 같습니다.
U: 위쪽으로 한 칸 가기
D: 아래쪽으로 한 칸 가기
R: 오른쪽으로 한 칸 가기
L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 
좌표평면의 경계는 
왼쪽 위(-5, 5), 
왼쪽 아래(-5, -5), 
오른쪽 위(5, 5), 
오른쪽 아래(5, -5)로 이루어져 있습니다.

명령어가 매개변수 dirs로 주어질 때, 
게임 캐릭터가 처음 걸어본 길의 길이를 구하여 
return 하는 solution 함수를 완성해 주세요.
"""


# 채점 결과
# 정확성: 25.0
# 합계: 25.0 / 100.0
def solution(dirs):
    answer = 0
    # 위, 아래, 오른쪽, 위쪽 방향키
    dd = ["U", "D", "R", "L"]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start = [0, 0]
    move = [[0,0]]

    for dir in dirs :
        meet = False
        idx = dd.index(dir)
        x, y = dx[idx], dy[idx]
        if (start[0]+x <= 5 and start[0]+x >= -5) and (start[1]+y <= 5 and start[1]+y >= -5) :
            start[0] +=x
            start[1] +=y
            result = start.copy()
            if result not in move :
                move.append(result)
            else :
                meet = True

    if not meet :
        answer = len(move)-1
    else :
        answer = len(move)

    return answer


# 채점 결과
# 정확성: 35.0
# 합계: 35.0 / 100.0
def solution(dirs):
    # 위, 아래, 오른쪽, 위쪽 방향키
    dd = ["U", "D", "R", "L"]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start = [0, 0]
    move = []

    for dir in dirs :
        idx = dd.index(dir)
        x, y = dx[idx], dy[idx]
        resultX = start[0]+x
        resultY = start[1]+y
        if (start[0]+x <= 5 and start[0]+x >= -5) and (start[1]+y <= 5 and start[1]+y >= -5) :
            start = [resultX, resultY]
            result = [resultX, resultY, dd[idx]]
            if result not in move :
                move.append(result)

    return len(move)


def solution(dirs):
    # 위, 아래, 오른쪽, 위쪽 방향키
    dd = ["U", "D", "R", "L"]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start = [0, 0]
    move = [[0,0]]
    answer = []

    for dir in dirs :
        idx = dd.index(dir)
        x, y = dx[idx], dy[idx]
        resultX = start[0]+x
        resultY = start[1]+y
        if (start[0]+x <= 5 and start[0]+x >= -5) and (start[1]+y <= 5 and start[1]+y >= -5) :
            start = [resultX, resultY]
            move.append(start)
    
    for i in range(len(move)-1) :
        first, second = move[i], move[i+1]
        value = first + second
        reversed_value = second + first
        if value not in answer and reversed_value not in answer :
            answer.append(value)

    return len(answer)

print(solution("ULURRDLLU"))
print("=="*10)
print(solution("LULLLLLLU"))
print(solution("RRRRRLLLLL"))



# 다른 사람 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2