"""
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
 "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
 
"""

def solution(s, n):
    upper = [chr(a+ord('A')) for a in range(26)]
    lower = [chr(a+ord('a')) for a in range(26)]
    answer = ''
    for st in s :
        if ord(st)==32 :
            answer +=" "
            continue
        if ord(st) <= 90 :
            answer += upper[(ord(st)-ord('A')+n)%26]
        else :
            answer += lower[(ord(st)-ord('a')+n)%26]
    return answer

def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer

print(solution("AB",1))
print(solution("z",1))
print(solution("a B z",4))

print(ord(" "))