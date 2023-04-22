"""
카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 
다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 
모두가 간단히 즐길 수 있다.
갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.

다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 
각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 
바로 전에 얻은 점수를 각 2배로 만든다. 
아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 
이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 
이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.
"""

# 합계: 93.8 / 100.0
def solution(dartResult):
    answer = 0
    result = []
    dart = []
    value = ""

    for d in dartResult :
        if not d.isdigit() :
            if len(value) >= 1 :
                dart.append(value)
            dart.append(d)
            value = ""
        else :
            value +=d
        
    print(dart)
    for i in range(len(dart)) :
        if dart[i].isdigit() :
            if dart[i+1] == "S" :
                result.append(int(dart[i]))
            elif dart[i+1] == "D" :
                result.append(int(dart[i])**2)
            elif dart[i+1] == "T" :
                result.append(int(dart[i])**3)
        elif dart[i] == "*" :
            if len(result) == 1 :
                result.append(result.pop()*2)
            else :
                value1 = result.pop()*2
                value2 = result.pop()*2
                result.append(value2)
                result.append(value1)

        elif dart[i] == "#" :
            result.append(result.pop()*(-1))

    for r in result :
        answer +=r
    
    print(result)
    return answer

# 다른 사람 풀이
from collections import deque

def solution(dartResult):
    answer = []
    d1 = dartResult
    n1 = ""

    for j in d1:
        n1 += j

        if j.isalpha():
            answer.append(n1[:-1])
            answer.append(j)
            n1 = ""
        if j == "*" or j == "#":
            answer.append(j)
            n1 = ""

    d2 = deque(answer)
    cnt = []
    for y in range(len(d2)):
        n2 = d2.popleft()

        if n2 == "S" and cnt:
            cnt[-1] = int(cnt[-1])**1
            continue
        if n2 == "D" and cnt:
            cnt[-1] = int(cnt[-1])**2
            continue
        if n2 == "T" and cnt:
            cnt[-1] = int(cnt[-1])**3
            continue

        cnt.append(n2)

    if "*" not in cnt and "#" not in cnt:
        return sum(cnt)

    final = []

    for j in cnt:
        if j == "#" and final:
            final[-1] = final[-1]*(-1)
            continue
        if j == "*" and final:
            if len(final) == 1:
                final[-1] = final[-1]*2
            if len(final) >= 2:
                final[-1] = final[-1]*2
                final[-2] = final[-2]*2

            continue

        final.append(j)
    return sum(final)



import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    # print(p)
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
        print(dart[i])
    answer = sum(dart)
    return answer

print(solution("1S2D3T"))
print(solution("1S2D#3T"))
print(solution("1S2D3T*"))
print(solution("1S*2D3T"))
print(solution("0S10S0S4S0S#0S#*"))
