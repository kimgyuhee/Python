"""
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, 
x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 
처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 
남은 부분이 없다면 종료합니다.
만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 
역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 
분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.
"""

from collections import deque
def solution(s):
    answer = 0
    dequeS = deque(s)

    yesX = 0
    noX = 0
    print(dequeS)
    for i in range(0, len(s)) :
        print("step0 >>> ", i)
        print("step1 >>> ",yesX, noX)
        if yesX == noX :
            answer +=1
            value1 = dequeS[i]
            yesX = 1
            noX = 0
            continue
        
        value2 = dequeS[i]
        print("step2 >>> ",value1, value1)
        if value2 == value1 :
            yesX +=1
        else :
            noX +=1

        print("step3 >>> ",yesX, noX)
    return answer


from collections import deque
def solution(s):
    answer = 0
    dequeS = deque(s)

    yesX = 0
    noX = 0
    for i in range(0, len(s)) :
        if yesX == noX :
            answer +=1
            value1 = dequeS[i]
            yesX = 1
            noX = 0
            continue
        
        value2 = dequeS[i]
        if value2 == value1 :
            yesX +=1
        else :
            noX +=1
    return answer


def solution(s):
    answer = 0
    yesX = 0
    noX = 0

    for i in range(0, len(s)) :
        if yesX == noX :
            answer +=1
            value1 = s[i]
            yesX = 1
            noX = 0
            continue
        
        value2 = s[i]
        if value2 == value1 :
            yesX +=1
        else :
            noX +=1
    return answer

# 다른 사람 풀이 1
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer

# 다른 사람 풀이 2
from collections import deque

def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))