"""
문자열 before와 after가 매개변수로 주어질 때, 
before의 순서를 바꾸어 after를 만들 수 있으면 1을, 
만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(before, after):
    case1 = ""
    case2 = ""
    for i in range(len(before)) :
        case1 +=before[len(before)-1-i]

    if case1 == after :
        return 1
    else :
        return 0
    
def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0 

print(solution("olleh", "hello"))
# print(solution("allpe", "apple"))
# print(solution("a", "a"))
# print(solution("a", "b"))