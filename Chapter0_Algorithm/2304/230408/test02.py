"""
문자열 s가 매개변수로 주어집니다. 
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
"""

def solution(s):
    answer = ''
    result = {}
    for r in s :
        if r not in result :
            result[r] = 1
            # print(result[r])
        else :
            result[r] +=1

    result = sorted(result.items())

    for r in result :
        # print(r)
        if r[1] == 1 :
            answer +=r[0]
    return answer

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer


print(solution("abcabcadc"))