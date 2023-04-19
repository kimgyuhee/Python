"""
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, 
solution을 완성하세요.
"""

def solution(s):
    answer = ''
    index = 0
    for str in s :
        if str == " " :
            index = 0
            answer +=str
            continue
        if index%2==0 :
            answer += str.upper()
        else :
            answer +=str.lower()
        index +=1
    return answer

print(solution("try hello world"))