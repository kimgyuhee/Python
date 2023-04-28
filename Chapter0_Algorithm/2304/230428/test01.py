"""
정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.
"""

def solution(num, n):
    answer = 1 if num%n == 0 else 0
    return answer

print(int(True))
print(int(False))

"""
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, 
flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, b, flag):
    if flag :
        return a+b
    else :
        return a-b
    
def solution(a, b, flag):
    return a+b if flag else a-b

"""
알파벳으로 이루어진 문자열 myString이 주어집니다. 
모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString):
    return myString.lower()

"""
1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 
두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.

a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, b):
    resta, restb = a%2, b%2
    print(a, b)
    if resta == 1 and restb == 1 :
        return a**2+b**2
    elif 1 in [resta, restb]:
        return 2*(a+b)
    else :
        return abs(a-b)
    
def solution(a, b):
    if a%2 and b%2: return a*a+b*b
    elif a%2 or b%2: return 2*(a+b)
    return abs(a-b)

print(solution(3, 5))

