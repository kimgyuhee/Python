"""
정수 배열 arr가 주어집니다. 
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 
50보다 작은 홀수라면 2를 곱합니다. 
그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

"""

def solution(arr):
    answer = []
    for a in arr :
        if a>=50 and a%2==0:
            answer.append(a//2)
        elif a<50 and a%2==1 :
            answer.append(a*2)
        else :
            answer.append(a)
    return answer

# 다른 사람 풀이
def solution(arr):
    return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]

"""
정수로 이루어진 리스트 num_list가 주어집니다. 
num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    answer = sorted(num_list)[5:]
    return answer

"""
한 자리 정수로 이루어진 문자열 num_str이 주어질 때,
각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_str):
    answer = 0
    for n in num_str :
        answer+=int(n)
    return answer

def solution(num_str):
    return sum(map(int, list(num_str)))

print(solution("1000000"))



def solution(start, end):
    return [i for i in range(start,end-1,-1)]

