"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 
return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr, queries):
    for a, b in queries :
        for i in range(a, b+1) :
            arr[i] +=1
    return arr

# 다른 사람 풀이
# import numpy as np
# def solution(arr, queries):
#     answer = []

#     arr = np.array(arr)
#     for query in queries:
#         arr[query[0]:query[1] + 1] += 1

#     answer = arr.tolist()
#     return answer

"""
문자열 my_string과 두 정수 m, c가 주어집니다. 
my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, m, c):
    answer = ''
    for i in range(c-1, len(my_string), m) :

        answer+=my_string[i]
    return answer

# 다른 사람 풀이
def solution(s, m, c):
    return s[c-1::m]

"""
정수가 있을 때, 짝수라면 반으로 나누고, 
홀수라면 1을 뺀 뒤 반으로 나누면, 
마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

10 / 2 = 5
(5 - 1) / 2 = 4
4 / 2 = 2
2 / 2 = 1
위와 같이 4번의 나누기 연산으로 1이 되었습니다.

정수들이 담긴 리스트 num_list가 주어질 때, 
num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 
return하도록 solution 함수를 완성해주세요.
"""

def make_one_n(num) :
    count = 0
    while num!=1 :
        if num%2 == 0 :
            num =num//2
        else :
            num = (num-1)//2
        count +=1
    return count+1

def solution(num_list):
    answer = 0
    for num in num_list :
        answer +=make_one_n(num)
    return answer

# 다른 사람 풀이
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

def solution(num_list):
    sum =0
    for i in num_list :
        b = bin(i)
        print(b)
        print(len(b))
        sum +=len(b)-3
    return sum

print(solution([12, 4, 150, 1, 14]))
