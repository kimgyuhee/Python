"""
정수로 이루어진 리스트 num_list가 주어집니다. 
num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 
return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    answer = sorted(num_list)
    return answer[:5]

"""
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 
return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_strings, parts):
    answer = ''
    for s, part in zip(my_strings, parts) :
        answer +=s[part[0]: part[1]+1]
    return answer

"""
단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, 
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 
return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string):
    answer = []
    string_list = my_string.split(" ")
    for s in string_list :
        if len(s) !=0 :
            answer.append(s)
    return answer

# 다른 사람 풀이
def solution(my_string):
    while '  ' in my_string:
        my_string = my_string.replace('  ', ' ')

    return my_string.strip().split()

"""
n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, 
arr이 다음을 만족하면 1을 아니라면 0을 
return 하는 solution 함수를 작성해 주세요.

0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
"""

def solution(arr):
    for i in range(len(arr)) :
        for j in range(len(arr)) :
            if arr[i][j] != arr[j][i] :
                return 0
    return 1


"""
문자열 binomial이 매개변수로 주어집니다. 
binomial은 "a op b" 형태의 이항식이고 
a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.
"""

def solution(binomial):
    answer = eval(binomial)
    return answer

# eval 함수 : 문지얄의 식을 계산한 결과를 반환해주는 함수

