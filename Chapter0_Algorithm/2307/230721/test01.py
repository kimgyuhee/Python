'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 
return 하도록 solution 함수를 완성해주세요.
'''

# 채점 결과
# 정확성: 83.3
# 합계: 83.3 / 100.0
# from itertools import combinations
from itertools import permutations
def primeNumber(number):
    result = True
    if number == 1 or number == 0 or number == 4:
        return False
    else :
        for i in range(2,number//2):
            if number%i == 0 :
                result = False
                break
    print(number, result)
    return result


def is_prime_num(n):
    if n == 0 or n == 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴


def solution(numbers):
    answer = 0
    cards = list(numbers)
    numbersList = []
    for i in range(1, len(numbers)+1) :
        comb = list(permutations(cards, i))
        for c in comb :
            number = "".join(c)
            if int(number) not in numbersList :
                numbersList.append(int(number))
                # result = primeNumber(int(number))
                result = is_prime_num(int(number))
                if result :
                    answer +=1
    return answer

print(solution("17"))
print(solution("011"))


for i in range(20) :
    r = is_prime_num(i)
    print(i, r)

"""
수학에서 에라토스테네스의 체는 소수를 찾는 방법이다. 고대 그리스 수학자 에라토스테네스가 발견하였다.
"""
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        print(a)
    a -= set(range(0, 2))
    print(a)
    print("="*20)
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
        print(a)
    return len(a)

print(solution("17"))
print(solution("011"))


from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
        print(a)
    a -= set(range(0, 2))
    print(a)
    print("="*20)
    for i in range(2, int(max(a) ** 0.5) + 1):
        print(a)
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

print(solution("1234"))
print(solution("011"))