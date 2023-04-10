"""
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다.
알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 
존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
"""

def solution(spell, dic):
    for d in dic :
        result = True
        print(d)
        for str in d :
            store = []
            print(str, end =" ")
            if str not in spell :
                result = False
                break
            else :
                if str not in store :
                    store.append(str)
                    if store.sort() == spell.sort() :
                        result = True
                        break
        print()
        if result :
            return 1
    return 2

# 다시 풀어보기
def solution(spell, dic):
    answer = 2
    for d in dic :
        result = True
        for s in spell :
            if s not in d :
                result = False
                break

        if result :
            answer = 1
            break
    return answer

# 다른 사람 문제 풀이
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))