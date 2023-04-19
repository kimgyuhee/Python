"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 
solution(3, 12)는 [3, 12]를 반환해야 합니다.
"""

def solution(n, m):
    answer = []
    for i in range(min(n,m)):
        k = min(n,m)-i
        if n%k == 0 and m%k==0 :
            answer.append(k)
            break

    if len(answer) == 0 :
        answer.append(1)
    
    answer.append(n//answer[0]*m//answer[0]*answer[0])
    return answer

from math import gcd
from math import lcm

def solution(a, b) :
    answer = []
    answer.append(gcd(a,b))
    answer.append(lcm(a,b))
    return answer

print(solution(3, 12))
print(solution(2, 5))
print(solution(1, 1))