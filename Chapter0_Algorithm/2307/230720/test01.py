"""
ROR 게임은 두 팀으로 나누어서 진행하며, 
상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 
따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다. 
다음은 5 x 5 크기의 맵에, 당신의 캐릭터가 (행: 1, 열: 1) 위치에 있고, 
상대 팀 진영은 (행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

위 그림에서 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다. 
캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 
게임 맵을 벗어난 길은 갈 수 없습니다.
아래 예시는 캐릭터가 상대 팀 진영으로 가는 두 가지 방법을 나타내고 있습니다.

만약, 상대 팀이 자신의 팀 진영 주위에 벽을 세워두었다면 
상대 팀 진영에 도착하지 못할 수도 있습니다. 
예를 들어, 다음과 같은 경우에 당신의 캐릭터는 상대 팀 진영에 도착할 수 없습니다.

게임 맵의 상태 maps가 매개변수로 주어질 때, 
캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 
return 하도록 solution 함수를 완성해주세요. 
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.
"""
"""

채점 결과
정확성: 16.5
효율성: 0.0
합계: 16.5 / 100.0
"""

# 아래, 오른쪽, 왼쪽, 위 -> 오른쪽, 아래쪽으로만 향하자
dx = [0,1,-1,0]
dy = [1,0,0,-1]
route = [[0,0]]
"""
def move(px, py, maps) :
    for i in range(4) :
        x = px + dx[i]
        y = py + dy[i]
        if (x >=0 and x <= 4) and (y >=0 and y <= 4) :
            if maps[x][y] != 0 :
                print(x, y)
                maps[px][py] = 0
                route.append([x, y])
                print("나강 !")
                return x, y
"""
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
mapsFinish = [[0,0,0,0,0]*5]
answer = 0
def move(px, py, maps) :
    global answer
    print(answer)
    for i in range(4) :
        x = px + dx[i]
        y = py + dy[i]
        if (x >=0 and x <= 4) and (y >=0 and y <= 4) :
            if maps[x][y] != 0 :
                answer +=1
                print(x, y)
                maps[px][py] = 0
                route.append([x, y])
                print("나강 !")
                move(x, y, maps)

move(0,0,maps)
print(answer)         
print(route)
print(route.index([4,4]))




print("=="*14)
dx = [0,1,-1,0]
dy = [1,0,0,-1]
route = [[0,0], [1,0]]


def solution(maps) :
    answer = 1
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    result = []
    route = [[0,0]]
    n = 20
    while n != 0 :
        n -=1
        # 종료조건
        if [4,4] in result :
            break
        elif len(route) == 0 :
            break

        pos = route.pop()
        for i in range(4) :
            x = pos[0] + dx[i]
            y = pos[1] + dy[i]
            if (x >=0 and x <= 4) and (y >=0 and y <= 4) :
                if maps[x][y] != 0 :
                    answer +=1
                    # print("eee", end="")
                    route.append([x, y])
                    result.append([x,y])
                    break


    if [4,4] not in result :
        result = []
        return -1

    print(result)
    
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

print(solution([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
print(solution([[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1]]))

print(solution([[1,0,1,1,1],[1,1,1,1,1],[0,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))