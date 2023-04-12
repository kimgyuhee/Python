"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다. 

정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
"""

from functools import reduce
from math import prod
def solution(arr):
    answer = 0
    for i in range(2, max(arr)+1):
        result = list(map(lambda x : x%2, arr))
        # print(result)
        if 1 not in result :
            result = list(map(lambda x : x//2, arr))
            answer = i
            break
    
    if answer !=0 :
        value = prod(result) * i
    else :
        value = prod(arr)

    return value

def solution(arr):
    answer = 0
    decimal = [2, 3, 5, 7]
    for d in decimal :
        result = list(map(lambda x : x%d, arr))
        if sum(result) == 0 :
            answer = d
            value = list(map(lambda x : x//d, arr))
            break

    if answer !=0 :
        return prod(value) * answer
    else :
        return prod(arr)


print(solution([2,6,8,14]))
print(solution([1,2,3]))
print(solution([1,2,3,4]))
print(solution([4]))
print(solution([2,7]))
print(solution([2,4]))