"""
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 
다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.
"""
# (x1 ∨ x2) ∧ (x3 ∨ x4)
def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer

# 다른 사람 풀이
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

"""
정수 배열 numLog가 주어집니다. 
처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 
순서대로 다음과 같은 조작을 했다고 합시다.

"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 
즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 
return 하는 solution 함수를 완성해 주세요.
"""
def solution(numLog):
    oper1 = {1:"w", -1:"s", 10:"d", -10:"a"}
    result = numLog[0]
    answer = ""
    for i in range(1, len(numLog)) :
        r = numLog[i] - result
        answer += oper1[r]
        result = numLog[i]
    print("wsdawsdassw" == answer)
    return answer

# 다른 사람 풀이 1
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res

# 다른 사람 풀이 2
def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1] # 현재 값과 이전 값의 차이를 계산
        if diff == 1:
            answer += 'w' # 1 더하기
        elif diff == -1:
            answer += 's' # 1 빼기
        elif diff == 10:
            answer += 'd' # 10 더하기
        elif diff == -10:
            answer += 'a' # 10 빼기
    return answer

print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))

"""
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 
예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.
"""
def solution(a, b):
    result1 = int(str(a)+str(b))
    result2 = 2*a*b
    return max(result1, result2)