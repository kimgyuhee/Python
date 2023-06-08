"""
itertools.permutations을 사용해 구현하는 법
"""
from itertools import permutations

# permutations(iterable, r)
# iterable의 원소들을 이용해 길이가 r인 순열을 생성한다.
# 리턴값은 순열 튜플의 이터레이터다.

data = "ABCD"
result = permutations(data, 2) # <itertools.permutations object at 0x7ff96110ee90>

for r in result:
    print(r)

"""
꼭 알아둬야 할 Python으로 순열 구현하는 법
재귀적으로 순열을 구현하는 법
"""

def permutation(arr, r):
    # 순열을 저장할 배열
    result = []
    # 실제 순열을 구하는 함수
    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return
        for idx, data in enumerate(arr):
            if idx not in index: 
                # list는 mutable이기 때문에 새로운 리스트를 넘겨준다.
                permute(p + [data], index + [idx])
    permute([], [])
    return result

for r in permutation(['A', 'B', 'C', 'D'], 2):
    print(r)


"""
꼭 알아둬야 할 Python으로 조합 구현하는 법
재귀적으로 조합을 구현하는 법
"""
# 재귀적으로 조합 구현

def combination(arr, r):
    
    # 조합을 저장할 배열
    result = []
    
    # 실제 조합을 구하는 함수
    def combinate(c, index):
        if len(c) == r:
            result.append(c)
            return 
        
        for idx, data in enumerate(arr):
            # 중복되는 조합이 생성되지 않게 마지막으로 들어온 원소의 인덱스보다
            # 새로 추가하는 원소의 인덱스가 큰 경우만 조합을 생성한다.
            if idx > index:
                combinate(c + [data], idx)
    
    combinate([], -1)
    
    return result

for r in combination(['A', 'B', 'C', 'D'], 2):
    print(r)

"""
itertools.combinations을 사용해 구현하는 법
"""

from itertools import combinations

# combinations(iterable, r)
# iterable의 원소들을 이용해 길이가 r인 조합을 생성한다.
# 리턴값은 조합 튜플의 이터레이터다.

data = "ABCD"
result = combinations(data, 2) # <itertools.combinations object at 0x7f603bdc5e90>

for r in result:
    print(r)

