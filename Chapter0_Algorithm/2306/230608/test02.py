"""
XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 
일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 
이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 
던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. 
"최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, 
"소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 
예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 
던전을 탐험한 후에는 피로도 20이 소모됩니다.

이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 
한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 
유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 
유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.
"""
# 완전탐색(브루트 포스)
# 모든 경우의 수를 탐색
# 전체 데이터 개수가 100만 개 이하일 때 사용

def solution(k, dungeons):
    answer = 0
    check = [False for _ in dungeons]
    # dungeons.sort(key=lambda x:x[1])
    # print(dungeons)

    for minimal_ph, ph in dungeons :
        if k >= minimal_ph :
            k = k-ph
            answer +=1

    return answer


from itertools import permutations

def solution(k, dungeons):
    answer = 0
    check = [False for _ in dungeons]
    # dungeons.sort(key=lambda x:x[1])
    # print(dungeons)

    all_dungeons = []
    for i in permutations(dungeons,len(dungeons)):
        all_dungeons.append(list(i))
    
    case = []
    for dungeon in all_dungeons :
        value = 0
        now_ph = k
        #print(dungeon)
        for minimal_ph, ph in dungeon :
            if now_ph >= minimal_ph :
                now_ph = now_ph-ph
                value +=1
        #print(value)
        case.append(value)

    return max(case)

print(solution(80, [[80,20],[50,40],[30,10]]))


# 다른 사람 풀이 1
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer