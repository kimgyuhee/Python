"""
정수 배열 array가 매개변수로 주어질 때,
가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array):
    answer = []
    m = max(array)
    index = array.index(m)
    return [m, index]


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

print("{0:=^20}".format("다음 문제"))
"""
머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 

n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 
최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(n):
    answer = 0
    if n == 1 :
        return 1
    for i in range(1, n) :
        if (6*i)%n == 0 :
            answer = i
            break
    return answer

def solution(n) :
    pizza = 1
    while (pizza * 6 % n) :
        pizza+=1
    return pizza

print(solution(6))
print(solution(100))
print(solution(12))
print(solution(10))
print(solution(4))
print(solution(1))