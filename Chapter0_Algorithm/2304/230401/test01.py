"""
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')'
문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
"""
def solution(s) :
    str = ""
    S = list(s)
    answer = False
    result = []
    for i in S :
        if i == "(" :
            result.append(i)
        elif i == ")" :
            try :
                str +=' '
                result.pop()
            except :
                return False
        else :
            str +=i

    print("괄호를 제외하고 남는 문자열 : ",str)

    if len(result) == 0 :
        answer = True

    return answer




print(solution("(hello)43"))
print(solution("(())()"))
print(solution("(())()"))
print(solution("(()("))

print(solution("(hello(name))(hihi)"))