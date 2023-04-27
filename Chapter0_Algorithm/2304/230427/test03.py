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
    print(calldata)

    for c in callings :
        calldata[c] -=1 

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))


d = {"ab" :2, "c":43, "ds" :43, "da":432, "fdsf" : 43}
print(d.get("ab"))
print(d.get("ab"))
print(d[1:3])