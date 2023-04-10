"""
머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 
예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(M, N):
    m = M-1
    n = M*(N-1)
    return n+m


print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))

"""
머쓱이는 RPG게임을 하고 있습니다. 
게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 
위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], 
left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에
캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 
예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 
오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
"""

def solution(keyinput, board):
    answer = [0,0]
    for k in keyinput :
        if k == "left" :
            if answer[0] != board[0]//2 * (-1) :
                answer[0] -=1
        elif k == "right" :
            if answer[0] != board[0]//2 :
                answer[0] +=1
        elif k == "up" :
            if answer[1] != board[1]//2 :
                answer[1] +=1
        elif k == "down" :
            if answer[1] != board[1]//2 *(-1) :
                answer[1] -=1
        
    return answer

# 다른 사람 풀이
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]


print(solution(["left", "right", "up", "right", "right"], [11,11]))
print(solution(["down", "down", "down", "down", "down"], [7,9]))
