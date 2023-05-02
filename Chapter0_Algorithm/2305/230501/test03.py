"""
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 
"n is even"을, 홀수이면 "n is odd."를 출력하는 코드를 작성해 보세요.
"""

a = int(input())

if a%2 == 0 :
    print(f"{a} is even")
else :
    print(f"{a} is odd")

# 다른 사람 풀이들
print(f"{a} is {'eovdedn'[a&1::2]}")
print(f"{a} is {'even' if a % 2 == 0 else 'odd'}")

"""
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, 
is_prefix가 my_string의 접두사라면 1을, 
아니면 0을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, is_prefix):
    answer = []
    for i in range(1, len(my_string)) :
        answer.append(my_string[:i])
    print(answer)
    if is_prefix in answer :
        return 1
    else :
        return 0
    
# 다른 사람 풀이
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
# startswith 처음보는 함수다.

"""
알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. 
myString의 연속된 부분 문자열 중 pat이 존재하면 1을 
그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.

단, 알파벳 대문자와 소문자는 구분하지 않습니다.

"""

def solution(myString, pat):
    if pat.lower() in myString.lower() :
        return 1
    else :
        return 0
    
def solution(myString, pat):
    return int(pat.lower() in myString.lower())
