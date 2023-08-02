from collections import deque

def div_2(value) :
    return value // 2

def div_3(value) :
    return value // 3

def sub_n(value, n) :
    return value - n

def solution(x, y, n):
    answer = 0
    if x == y :
        return 0
    valueToCalculate = deque([y])
    valueList = [y]
    while True :
        value = valueToCalculate.popleft()
        # print(f"계산할 값은 {value}입니다.")
        a = div_2(value)
        b = div_3(value)
        c = sub_n(value, n)
        valueList += [a, b, c]
        valueToCalculate.append(a)
        valueToCalculate.append(b)
        valueToCalculate.append(c)
        answer +=1
        if x in [a, b, c] or (a < 1 and b < 1 and c < 1) : # 종료조건
            break

    print(valueList)

    if y not in valueList :
        return -1
    
    return answer

print(solution(10, 38, 2)) # 2
print(solution(10, 40, 5)) # 2
print(solution(10, 40, 30)) # 1
print(solution(2, 5, 4)) # -1
print(solution(38, 40, 2)) # 1
print(solution(38, 40, 2)) # 1
print(solution(38, 38, 2)) # 1