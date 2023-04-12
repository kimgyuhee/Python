"""
문자열 my_str과 n이 매개변수로 주어질 때, 
my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_str, n):
    # answer = list(my_str, n)

    answer = []
    index = 0
    combination = ""
    for s in my_str :
        if index == n :
            answer.append(combination)
            combination = ""
            index = 0
        combination +=s
        index +=1
    
    if len(combination) != 0 :
        answer.append(combination)
    return answer


# 다른 사람 풀이
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer


def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))