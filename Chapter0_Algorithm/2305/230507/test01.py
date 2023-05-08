"""
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 
나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, 
return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.
"""

import re


def solution(myStr):
    answer = []
    myStr = myStr.replace("a", " ")
    myStr = myStr.replace("b", " ")
    myStr = myStr.replace("c", " ")
    
    my_string = myStr.split(" ")
    for ms in my_string :
        if ms != "" :
            answer.append(ms)

    if len(answer) == 0 :
        return ["EMPTY"]
    else :
        return answer
    

# 다른 사람 풀이
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']

print(solution("baconlettucetomato"))

"""
문자열 myString과 pat가 주어집니다. 
myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString, pat):
    idx = myString[::-1].find(pat[::-1])
    print(idx)
    if idx == 0 :
        return myString
    else :
        return myString[:-idx]

# 다른 사람 풀이 1
solution=lambda x,y:x[:x.rindex(y)+len(y)]

# 다른 사람 풀이 2
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

print(solution("AbCdaadEFG", "dE"))
print(solution("AAAAaaaa", "a"))

"""
다음과 같이 출력하도록 코드를 작성해 주세요.

>>> 출력예시
>>> !@#$%^&*(\'"<>?:;
"""

print('hello world!')
print("!@#$%^&*(\\\'\"<>?:;")

# 공백 기준 분리
text = "사과 딸기 수박 메론 바나나"
t = re.split(" ", text)
print(text)
print(t)

"""
문자열 myString과 pat이 주어집니다.
myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString, pat):
    answer = 0
    for i in range(len(myString)-len(pat)+1) :
        print(myString[i:i+len(pat)+1])
        if pat == myString[i:i+len(pat)] :
            answer +=1
    return answer

print(solution("banana", "ana"))