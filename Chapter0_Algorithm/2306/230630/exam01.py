"""
멘토 n명이 존재
1~k 상담 유형
멘토 : k 상담 유형 중 1개만 담당

"""
from itertools import permutations

def sum_case(k, n) : # 2, 3
    answer = []
    if k==0: #혹시 k=0을 넣을 수도 있으니까요^^ 이럴 경우 그냥 0을 리턴한다고 가정합니다.
        return 0
    if k==1: #변수가 한개만 남았을 경우 1가지만 가능하므로 1을 리턴합니다.
        return 1
    count = 0 #카운터 변수를 초기화 시키고,

    #a_1이 가능한 0에서 n까지 반복하여 값을 대입하면서 recursive call을 합니다.
    for i in range(n+1):
        count += sum_case(n-i, k-1)
    return count

print(sum_case(3, 2))



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