"""
문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 
return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, index_list):
    answer = ''
    for i in index_list :
        answer +=my_string[i]
    return answer

# 다른 사람 풀이 1
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

"""
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. 
myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 
pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
"""

def solution(myString, pat):
    answer = 0
    changeString = ""
    for m in myString :
        if m == "A" :
            changeString +="B"
        elif m == "B" :
            changeString +="A"

        if pat in changeString :
            return 1
    return answer

# 다른 사람 풀이 
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))


"""
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 
예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 
return 하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
"""

def solution(a, b):
    answer1 = str(a)+str(b)
    answer2 = str(b)+str(a)

    return max(int(answer1), int(answer2))

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

"""
문자열 my_string과 정수 배열 indices가 주어질 때,
my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 
이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, indices):
    result = ""
    answer = [s for s in my_string]
    ox = [False if i in indices else True for i in range(len(my_string))]
    print(ox)
    for a, xo in zip(answer, ox) :
        print(xo, a)
        if xo :
            result +=a
    return result

print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))

# 다른 사람 풀이
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer