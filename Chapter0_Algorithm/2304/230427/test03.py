"""
얀에서는 매년 달리기 경주가 열립니다. 
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 
해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

"""
# 시간 초과
# 합계: 68.8 / 100.0
def solution(players, callings):
    for c in callings :
        overtake_index = players.index(c)
        overtaken = players[overtake_index-1]

        players[overtake_index-1], players[overtake_index] = c, overtaken
        print(players)
    return players


def solution(players, callings):
    answer = []
    calldata = {players[i] : i for i in range(len(players))}
    st = {players[i] : i for i in range(len(players))}

    for c in callings :
        calldata[c] -=1 

    print(calldata)
    print(st)
    for a, b in zip(calldata.items(), st.items()) :
        if a == b :
            answer.append(a[0])
        else :
            answer.insert(a[1], a[0])
    return answer


def solution(players, callings):
    answer = []
    calldata = {players[i] : i for i in range(len(players))}
    st = {players[i] : i for i in range(len(players))}

    for c in callings :
        calldata[c] -=1 

    for a, b in zip(calldata.items(), st.items()) :
        if a == b :
            answer.append(a[0])
        else :
            answer.insert(a[1], a[0])
    return answer


# 다른 사람 풀이 1
def solution(players, callings):
    answer = []
    hashmap = dict()
    for i,v in enumerate(players):
        hashmap[v] = i 
    for call in callings:
        pre,post = hashmap[call] - 1,hashmap[call]
        hashmap[players[pre]] = post
        hashmap[players[post]] = pre
        players[pre],players[post] = players[post],players[pre]
    return players


def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}

    for j in callings:
        current_index = player_indices[j]
        desired_index = current_index - 1
        if current_index > 0 and players[desired_index] != j:
            players[current_index], players[desired_index] = players[desired_index], players[current_index]
            player_indices[players[current_index]] = current_index
            player_indices[players[desired_index]] = desired_index

    return players

# 다른 사람 풀이 3
def solution(players, callings):
    answer = []

    p_dic = {player:i+1 for i,player in enumerate(players)}
    location_dic = {i+1:player for i,player in enumerate(players)}

    for c in callings:
        c_loc = p_dic[c]
        front = c_loc - 1
        front_p = location_dic[front]
        p_dic[c] -= 1
        p_dic[front_p] += 1
        location_dic[c_loc] = front_p
        location_dic[front] = c



    p_dic = dict(sorted(p_dic.items(),key=lambda x:x[1]))
    answer = list(p_dic.keys())

    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))


d = {"ab" :2, "c":43, "ds" :43, "da":432, "fdsf" : 43}
print(d.get("ab"))
print(d.get("ab"))
# print(d[1:3])

f = [23,4,3,5,2,1]
f = [23,4,3,5,2,1]
f.insert(1,0)
print(f)