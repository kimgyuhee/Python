"""
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
정수 n이 주어질 때 다음 조건을 만족하는 
가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

i! ≤ n

"""

def solution(n):
    answer = [0 for _ in range(10)]
    mul = 1
    index = 0
    for i in range(1, 11) :
        mul *=i
        answer[i-1] = mul
        if n <= mul :
            index = i
            break

    if answer[index-1] == n :
        return index
    else :
        return index-1


from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

print(solution(3628800))
print(solution(7))