"""
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
"""

def solution(a, b):
    def maxValue(a, b) :
        if a > b :
            return a, b
        else :
            return b, a
        
    v1, v2 = maxValue(a, b)
    # print(v1, v2)
    answer = []
    for i in range(v2, v1+1) :
        if i not in answer :
            answer.append(i)
    return sum(answer)

def solution(a, b):
    answer = [i for i in range(min(a,b), max(a, b)+1)]
    return sum(answer)

print(solution(3, 5))
print(solution(5, 3))
print(solution(3, 3))