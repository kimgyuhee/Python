"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 
두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 
return 하도록 solution 함수를 완성해보세요.
"""

def solution(numer1, denom1, numer2, denom2):
    def findMax(a, b) :
        if a > b :
            return a, b
        else :
            return b, a
        
    maxD, minD = findMax(denom1, denom2)
    if maxD % minD == 0 :
        denom = maxD
    else :
        for d in range(2, denom1*denom2+1) :
            if d%denom1 == 0 and d%denom2 == 0 :
                denom = d
                break
    
    numer = (denom//denom1)*numer1 + (denom//denom2)*numer2

    return [numer, denom]

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = denom2*numer1 + denom1*numer2

    for i in range(2, 10) :
        if denom%i == 0 and numer%i == 0 :
            while denom%i == 0 and numer%i == 0 :
                denom //=i
                numer //=i

    return [numer, denom]


def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = denom2*numer1 + denom1*numer2
    gcd = 1

    for i in range(1, numer+1) :
        if denom%i == 0 and numer%i == 0 :
           gcd = i

    return [numer//gcd, denom//gcd]

# 다른 사람 풀이

import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
print(solution(9, 4, 1, 4))

print(2%4)