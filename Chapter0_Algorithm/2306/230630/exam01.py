"""
멘토 n명이 존재
1~k 상담 유형
멘토 : k 상담 유형 중 1개만 담당

"""
from itertools import permutations

def sum_case(k, n) : # 2, 3
    pass
#print(sum_case(3, 2))



def solution(k, n, reqs) :
    answer = 0
    # 경우의 수 구하기
    category = [1] * k
    case = list(permutations(range(n-k),k))
    print(case)
    print(category)
    dict_sort = {i+1 : [] for i in range(k)}
    print(dict_sort)
    for r in reqs :
        dict_sort[r[2]].append(r)
    print(dict_sort)
    return answer

print(solution(2, 3, [[5,55,2], [10, 90, 2], [20,40,2], [50,45,2],[100,50,2]]))

"""
a = list(permutations(range(5), 3))
print(a)
"""