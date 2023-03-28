"""
나만의 카카오 성격 유형 검사지를 만들려고 합니다.
성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서 두 유형 중 하나로 결정됩니다.

//AN
매우 비동의     어피치형 3점                         #1
비동의         어피치형 2점                         #2
약간 비동의     어피치형 1점                         #3
모르겠음        어떤 성격 유형도 점수를 얻지 않습니다      #4   
약간 동의       네오형 1점                          #5
동의	       네오형 2점                          #6
매우 동의	    네오형 3점                          #7
"""

def solution(survey, choices):
    q = [["R","T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    answer = ''
    dict = {}
    for i in range(0, len(survey)):
        a, b = survey[i][0], survey[i][1]
        print(a, b)
        if choices[i] > 4 :
            dict[b] = abs(choices[i]-4)
        elif choices[i] < 4 :
            dict[a] = abs(choices[i]-4)
    print("확인중!!!!!!!!!!!!")
    for a, b in q :
        print(a, b, " -> ", dict.get(a), dict.get(b))
        if (dict.get(a)  == None) :
            dict[a] = 0
        if (dict.get(b)  == None) :
            dict[b] = 0

    print(dict)

    for a, b in q : 
        print(a, b)
        print(type(dict.get(a)), type(dict.get(b)))
        if dict.get(a) >= dict.get(b) :
            answer += a
        else :
            answer +=b

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))

## 깔끔하다....
def solution1(survey, choices):
    answer = ''
    dicts = {'T' : 0, 'R' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for i in range(len(survey)) : 
        if choices[i] - 4 < 0: # choices 값이 4 미만일 시, survey의 앞의 값 출력
            dicts[survey[i][0]] += 4 - choices[i]

        elif choices[i] - 4 > 0: # choices 값이 4 초과 시, survey의 앞의 값 출력
            dicts[survey[i][1]] += choices[i] - 4

    answer += 'R' if dicts['R'] >= dicts['T'] else 'T'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'

    return answer
