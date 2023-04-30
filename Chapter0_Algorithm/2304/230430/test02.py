"""
정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 
음수가 없다면 -1을 return합니다.
"""

def solution(num_list):
    answer = -1
    for n in num_list :
        if n < 0 :
            answer = num_list.index(n)
            break
    return answer



"""
정수 start와 end가 주어질 때, start부터 end까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
"""

def solution(start, end):
    answer = [i for i in range(start, end+1)]
    return answer

"""
정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

"""

def solution(n, control):
    answer = n
    keys = {"w" : 1, "s" : -1, "d" : 10, "a" : -10} 
    for c in control :
        answer+=keys[c]

    return answer


def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])