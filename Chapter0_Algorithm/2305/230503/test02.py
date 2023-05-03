"""
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string이 매개변수로 주어질 때, 
my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string):
    answer = []
    for i in range(len(my_string)) :
        answer.append(my_string[i:])
    return sorted(answer)

# 다른 사람 풀이 : 한줄
def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))

"""
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, overwrite_string, s):
    answer = my_string[:s]+overwrite_string + my_string[s+len(overwrite_string):]
    return answer

"""
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 
세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 
얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 
(a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 
(a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 
얻는 점수를 return 하는 solution 함수를 작성해 주세요.
"""
def solution(a, b, c):
    answer = 0
    if a == b == c :
        answer = (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3 )
    elif a == b != c or a != b == c or b != a == c :
        answer = (a + b + c) * (a**2 + b**2 + c**2 )
    else :
        answer = a+b+c
    return answer

# 다른 사람 풀이
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)