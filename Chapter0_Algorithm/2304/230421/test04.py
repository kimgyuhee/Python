"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

from itertools import combinations

def solution(nums):
    answer = 0
    combis = list(combinations(nums, 3))
    for c in combis :
        num = sum(c)
        result = True
        for n in range(2, num) :
            if num % n == 0 :
                result = False
                break
        if result :
            answer +=1

    return answer

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

print(solution([1,2,7,6,4]))