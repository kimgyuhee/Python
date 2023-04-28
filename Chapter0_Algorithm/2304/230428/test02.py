"""
문자열 my_string과 정수 k가 주어질 때, 
my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, k):
    answer = len(k) // len(my_string)
    return answer

print(solution("string", "stringstringstring"))

"""
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, n):
    answer = my_string[-n:]
    return answer

print(solution("ProgrammerS123", 11))

def solution(flo):
    return flo - int(flo)

def solution(flo):
    return flo%1

def solution(flo):
    n = len(str(flo))-1
    m = len(str(int(flo)))
    return round(flo%1, n-m)

def solution(flo):
    n = len(str(flo))-1
    m = len(str(int(flo)))
    return round(flo%1, n-m)

print(solution(1.43))


def solution(num_list, n):
    answer = num_list[:n]
    return answer


import math

def solution(num_list):
    answer1 = sum(num_list)**2
    answer2 = math.prod(num_list)
    return 1 if answer1 > answer2 else 0

# 다른 사람 풀이
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0
 
print(solution([3, 4, 5, 2, 1]))


