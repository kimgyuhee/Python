"""
문자열 my_string이 매개변수로 주어집니다.
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

"""

def solution(my_string):
    answer = ""
    sum = 0
    for s in my_string :
        if s.isdigit() :
            print(s)
            answer +=s
        else :
            if len(answer) > 0 :
                print(">>> ",int(answer))
                sum += int(answer)
            answer = ""

    if len(answer) != 0 :
        sum+=int(answer)

    return sum


# 다른 사람 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    print(s)
    return sum(int(i) for i in s.split())

def solution(my_string):
    sum = 0
    for s in my_string :
        if not s.isdigit() :
            my_string = my_string.replace(s, " ")

    # print(my_string)
    l = my_string.split(" ")
    for i in l :
        if i.isdigit() :
            sum+=int(i)
    # print(l)
    return sum




print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))
print(solution("1234"))
print(solution("s"))

a = ""