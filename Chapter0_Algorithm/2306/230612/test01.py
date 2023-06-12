"""

양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 
변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

0P0처럼 소수 양쪽에 0이 있는 경우
P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
P처럼 소수 양쪽에 아무것도 없는 경우
단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
예를 들어, 101은 P가 될 수 없습니다.
예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 
여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 
총 3개입니다. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.

정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 
변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 
return 하도록 solution 함수를 완성해 주세요.
"""
# 채점 결과
# 정확성: 88.1
# 합계: 88.1 / 100.0
# 소수 구하는 함수
def decimal(num) :
    if num == 1 :
        return False
    for i in range(2, num//2) :
        if num%i == 0 :
            return False
    return True

# 10진수를 k진수로 변환
def base_conversion(num, k) :
    rev_base = ''

    while num > 0 :
        num, mod = divmod(num, k)
        rev_base +=str(mod)

    return rev_base[::-1]

def solution(n, k):
    answer = 0
    base = base_conversion(n, k)
    base_list = base.split("0")
    for b in base_list :
        if b == "" :
            continue
        else :
            if decimal(int(b)) :
                answer +=1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(110000000101, 10))
"""
2, 8, 16진수는 bin(), oct(), hex() 함수를 지원한다.
print(bin(11)) # 0b1011
print(oct(11)) # 0o13
print(hex(11)) # 0xb
"""