"""
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
"""
print(int('101',2))
print(int('202',3))
print(int('303',4))
print(int('404',5))
print(int('505',6))
print(int('ACF',16))

def baseConversion(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def solution(n):
    answer = baseConversion(n,3)
    result = answer[::-1]
    return int(result, 3)


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3
        print(tmp, n)

    answer = int(tmp, 3)
    return answer

print(solution(45))
print(solution(125))