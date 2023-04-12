"""
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 
담은 배열을 return하도록 solution 함수를 완성해주세요.
"""

#   몇몇 케이스 런타임 에러
def solution(quiz):
    answer = []
    for q in quiz :
        listQ = q.replace("- ", "-").replace("+ ", "").split(" ")
        sum = 0
        for l in listQ :
            if l == "=" :
                break
            sum +=int(l)
        if sum == int(listQ[len(listQ)-1]) :
            answer.append("O")
        else :
            answer.append("X")
    return answer


def solution(quiz):
    def OX(tf) :
        if tf :
            return "O"
        else :
            return "X"

    answer = []
    for q in quiz :
        listQ = q.split(" ")
        sum = 0
        if listQ[1] == "+" :
            sum = int(listQ[0]) +int(listQ[2])
            answer.append(OX(sum == int(listQ[4])))
        elif listQ[1] == "-":
            sum = int(listQ[0]) - int(listQ[2])
            answer.append(OX(sum == int(listQ[4])))
        else :
            print("에러")
    return answer


# 다른 사람 풀이 
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]  

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))