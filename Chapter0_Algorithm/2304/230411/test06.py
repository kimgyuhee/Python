"""
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 
분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 
유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 a와 b가 매개변수로 주어질 때, 
a/b가 유한소수이면 1을, 
무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

"""
def factorize2(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  # 에라토스테네스를 떠올리며,, 즉 루트n까지 실행
        while (n % factor == 0):  # 소수로 나누어 떨어지면(= 즉 약수면)
            factors.append(factor)  # 리스트에 추가
            n = n // factor  # n을 몫으로 변경
            factor += 1
    if n > 1 : # 1보다 크고 factor**2(4)보다 작은 경우 n은 소수임으로 append -> 2,3 경우
        factors.append(n)
    return factors

def factorization(n):
    i = 2
    factor = []
    while n != 1:
        if n % i == 0:
            n //= i
            factor.append(i)
        else:
            i += 1
    return factor

def solution(a, b):
    answer = 0
    for n in range(2, a+1) :
        if a%n == 0 and b%n == 0 :
            a //=n
            b //=n
    # print("qqqqqq")
    result = factorization(b)
    # print("dld")
    result = set(result)
    print(result)
    store = [{2, 5}, {2}, {5}, set()]
    if result in store :
        return 1
    else :
        return 2
    
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    print(b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 1))
print(solution(12, 12))
print(solution(3500, 500))



"""
def factorize2(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  # 에라토스테네스를 떠올리며,, 즉 루트n까지 실행
        while (n % factor == 0):  # 소수로 나누어 떨어지면(= 즉 약수면)
            factors.append(factor)  # 리스트에 추가
            n = n // factor  # n을 몫으로 변경
            factor += 1
    if n > 1 : # 1보다 크고 factor**2(4)보다 작은 경우 n은 소수임으로 append -> 2,3 경우
        factors.append(n)
    return factors

print('효율적인 소인수분해 결과', factorize2(30))
"""