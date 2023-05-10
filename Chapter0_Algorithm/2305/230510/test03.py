"""
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 
각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
"""

str = input()
answer = ""
for s in str :
    if s.isupper() :
        answer+=s.lower()
    else :
        answer+=s.upper()

print(answer)

# 다른 사람 코드 1
print(input().swapcase())

"""
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 
'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string):
    answer = [0 for _ in range(52)]
    # print(answer)
    for s in my_string :
        if ord(s) <=90 :
            answer[ord(s)-65] +=1
        else :
            answer[ord(s)-97] +=1
    return answer

print(solution("Programmers"))

print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122