"""
n개의 음이 아닌 정수들이 있습니다. 
이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 
return 하도록 solution 함수를 작성해주세요.

"""
from itertools import permutations # 순열
from itertools import combinations # 조합

def solution(numbers, target):
    count = 0
    for i in range(len(numbers)+1) :
        cases = combinations(numbers, i)
        for case in cases :
            plus = list(case)
            minus = numbers.copy()
            for p in plus :
                minus.remove(p)
            
            if sum(plus)-sum(minus) == target :
                count +=1

    return count

    
# 다른 사람 풀이2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    print(*l)
    s = list(map(sum, product(*l)))
    print(s)
    return s.count(target)

"""
product 
"""


# 다른 사람 풀이1
def solution(numbers, target):
    print(f"========== number : {numbers}, target : {target} ===============")
    if not numbers and target == 0 :
        print("어려워요")
        return 1
    elif not numbers:
        print("not number")
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
print(solution([1, 1, 1, 1, 1], 3))
print("="*50)
print(solution([4, 1, 2, 1], 4))


from itertools import product

data = ['사과', '배', '귤']

result = list(product(*data))
data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = list(product(*data1))

print(result)
