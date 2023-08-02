"""
https://school.programmers.co.kr/learn/courses/30/lessons/154538
숫자 변환하기
문제 설명
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, 
x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 
이때 x를 y로 만들 수 없다면 -1을 return 해주세요.
0
1       2       3           -> [1] 3    (1 ~ 3)
4 5 6   7 8 9   10 11 12    -> [2] 9    (4 ~ 12) 
13                             -> [3] 27   (13 ~ 40)
"""
from collections import deque

def mul_2(value) :
    return 2 * value

def mul_3(value) :
    return 3 * value

def add_n(value, n) :
    return value + n

def treeDepth(idx) :
    v3 = 3
    depth = 1
    while True :
        if idx <= v3 :
            break
        depth +=1
        v3 += 3**depth

    return depth
    

def solution(x, y, n):
    answer = 0
    if x == y :
        return 0
    valueToCalculate = deque([x])
    valueList = [x]
    while len(valueToCalculate) :
        value = valueToCalculate.popleft()
        # print(f"계산할 값은 {value}입니다.")
        a = mul_2(value)
        b = mul_3(value)
        c = add_n(value, n)
        valueList += [a, b, c]
        if a <= y or b <= y or c <=y :
            valueToCalculate.append(a)
            valueToCalculate.append(b)
            valueToCalculate.append(c)
        answer +=1
        if y in [a, b, c] : # 종료조건
            break

    print(valueList)
    if y not in valueList :
        return -1
    else :
        idx = valueList.index(y)
        print(idx)
        return treeDepth(idx)
    

print(solution(10, 38, 2)) # 2
print(solution(10, 40, 5)) # 2
print(solution(10, 40, 30)) # 1
print(solution(2, 5, 4)) # -1
print(solution(38, 40, 2)) # 1
print(solution(38, 40, 2)) # 1
print(solution(38, 38, 2)) # 1


print("tree 깊이 알아보기")
for i in range(1, 42) :
    print(i, treeDepth(i))