"""
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다.
이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, 
A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 
밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

"""

def solution(A, B):
    answer = 0
    for i in range(len(A)) :
        if A == B :
            break
        A = A[-(i+1):] + A[:-(i+1)]
        print(A)
        answer +=1

    if len(A) == answer :
        return -1

    return answer

from collections import deque

def solution(A, B):
    a = deque(A)
    b = deque(B)
    answer = 0
    for i in range(len(A)) :
        if a == b :
            break
        answer +=1
        value = a.pop()
        a.appendleft(value)
        print(a)

    if len(A) == answer :
        return -1
    return answer

# 다른 사람 풀이 1
solution=lambda a,b:(b*2).find(a)

# 다른 사람 풀이 2


print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("abc", "bca"))
