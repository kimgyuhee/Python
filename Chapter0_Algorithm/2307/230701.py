"""
0 또는 양의 정수가 주어졌을 때, 
정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 
문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
"""
from itertools import permutations
def solution(numbers):
    answer = ''
    for n in numbers :
        answer+=str(n)
    
    p_list = list(permutations(answer,len(answer)))
    # print(p_list)
    #store_number = []
    result = 0
    for p in p_list :
        # print(p, type(p))
        num = ""
        for n in p :
            num +=n
        if result <= int(num) :
            result = int(num)
    return result



# 채점 결과
# 정확성: 26.7
# 합계: 26.7 / 100.0
# 나머지 시간 초과
from itertools import permutations
def solution(numbers):
    answer = 0
    p_list = list(permutations(numbers,len(numbers)))

    for p in p_list :
        num = ""
        for n in p :
            num +=str(n)
        if answer <= int(num) :
            answer = int(num)
    return str(answer)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))