"""
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때,
수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
"""

def solution(my_string):
    list = my_string.split(" ")
    
    if list[1] == "+" :
        sum = int(list[0]) + int(list[2])
    elif list[1] == "-" :
        sum = int(list[0]) - int(list[2])

    if len(list) == 3 :
        return sum
    
    for i in range(3, len(list)) :
        if not list[i].isdigit() :
            if list[i] == "+" :
                sum +=int(list[i+1])
            elif list[i] == "-" :
                sum -=int(list[i+1])
    return sum

# 다른 사람 풀이1
solution=eval

# 다른 사람 풀이2
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# 다른 사람 풀이3
def solution(my_string):
    print(my_string.replace("-", "+ -"))
    print(my_string.replace("-", "+ -").split("+"))
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))


print(solution("3 + 4"))
print(solution("3 + 4 - 3 + 5"))

a = [- 1 , 3]
print(a)
print(sum(a))
