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


def solution(numbers):
    answer = ""
    digit_2 = []
    for n in numbers :
        value = bin(n)
        digit_2.append(value[2:])
    digit_2.sort(key=len)
    print(digit_2[::-1])
    for d in digit_2[::-1] :
        value = int(d, 2)
        answer +=str(value)
    return str(answer)

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




# 채점 결과
# 정확성: 53.3
# 합계: 53.3 / 100.0

from itertools import permutations
def find_combin_max(value) :
    case_list = list(permutations(value,len(value)))
    result = 0
    for case in case_list :
        value = "".join(list(map(str, case)))
        if result < int(value) :
            result = int(value)
    return result

def solution(numbers):
    answer = ""
    num_dict = {9-i:[] for i in range(10)}
    num_str_list = list(map(str, numbers))
    for msl in num_str_list :
        num_dict[int(msl[0])].append(int(msl))

    for value in num_dict.values() :
        if len(value)!=0 :
            result = find_combin_max(value)
            answer +=str(result)

    return answer


n = [1, 211, 34, 1000, 999]
for num in n :
    d = len(str(num))
    print(num, d)
    if num <= 10 :
        if num%10 == 0 :
            key = num//10
        else :
            key = num%10
    else :
        key = num//(10**(d-1))
    print(key)

numbers = [1, 211, 34, 43, 1000, 999]
numbers = list(map(str, numbers))
for number in numbers :
    print("=="*10)
    print(number * 4)
    print((number * 4)[:4])
numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
print(numbers)


# 다른 사람 풀이...
# 천재 인정
def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0':
        return '0'
    else:
        return answer
print(solution([6, 10, 2]))
print(solution([17, 18, 2]))
print(solution([3, 30, 34, 5, 9]))