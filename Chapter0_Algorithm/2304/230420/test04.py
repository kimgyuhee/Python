"""
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 
더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 
return 하도록 solution 함수를 완성해주세요.

"""

from itertools import combinations
def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    for c in combi :
        value = sum(c)
        if value not in answer :
            answer.append(value)
    return sorted(answer)


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))