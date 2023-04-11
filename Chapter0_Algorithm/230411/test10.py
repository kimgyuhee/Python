"""
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 
동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
같은 식이라면 가장 짧은 수식을 return 합니다.
"""

# 100점 중에 75점...
def solution(polynomial):
    answer = []
    n = 0
    poly = polynomial.replace("+ ", "").split(" ")
    for p in poly :
        if "x" in p :
            if "x" == p :
                answer.append(1)
            else :
                answer.append(int(p[:-1]))
        else :
            n +=int(p)

    if n == 0 :
        if sum(answer) == 1 :
            result = "x"
        elif sum(answer) == 0 :
            return
        else :
            result = f"{sum(answer)}x"
    elif sum(answer) == 0 :
        result = n
    elif sum(answer) == 1 :
        result = f"x + {n}"
    else :
        result = f"{sum(answer)}x + {n}"

    return result

# 다른 사람 풀이 1
def solution(polynomial):
    x, num = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if 'x' not in i:
            num += int(i)
        else:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    if x == 0 and num == 0:
        return
    if x == 0:
        return str(num)
    if x == 1:
        x = ""
    if num == 0:
        return str(x) + "x"
    return str(x) + "x + " + str(num)

# 다른 사람 풀이 2
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'

print(solution("3x + 7 + x"))
print(solution("x + x + x"))
print(solution("x + x + x + 9 + 5x + 6x + 11 + 100x"))
print(solution("10 + 4"))
print(solution("1 + 4 + 99 + x"))
print(solution("1"))
print(solution("x"))
print(solution("0 + 0 + 550x + 0 + 0x"))
print(solution("0 + x + 1"))