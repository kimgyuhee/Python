"""
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 
양의 정수 배열 arr가 매개변수로 주어질 때, 
arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 
X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 
return 하는 solution 함수를 작성해 주세요.
"""


def solution(arr):
    answer = []
    for a in arr :
        for i in range(a) :
            answer.append(a)
    return answer

n = [3] * 3
print(n + [3])

# 다른 사람 풀이
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer

"""
문자열 myString이 주어집니다. 
myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, 
"A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 
return 하는 solution 함수를 완성하세요.
"""

def solution(myString):
    answer = ''
    for s in myString.lower() :
        if s == "a" :
            answer +=s.upper()
            continue
        answer+=s
    return answer

# 다른 사람 풀이
def solution(myString):
    return myString.lower().replace('a', 'A')

"""
길이가 같은 두 문자열 str1과 str2가 주어집니다.

두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 
한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
"""

def solution(str1, str2):
    answer = ''
    for a, b in zip(str1, str2) :
        answer +=(a+b)
    return answer

# 다른 사람 풀이
def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer
