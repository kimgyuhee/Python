"""
2개 이하로 다른 비트
문제 설명
양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.

x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
예를 들어,

f(2) = 3 입니다. 
다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 
제일 작은 수가 3이기 때문입니다.

정수들이 담긴 배열 numbers가 매개변수로 주어집니다. numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

"""
# 채점 결과
# 정확성: 81.8
# 합계: 81.8 / 100.0
# => 시간초과로 실패
"""
compare 메소드 코드 수정
if diff >=3 :
    break
"""
def compare(value, other) :
    diff = 0
    l = len(value) if len(value) > len(other) else len(other)
    value = value.zfill(l)
    other = other.zfill(l)
    for i in range(l) :
        if diff >=3 :
            break
        if value[i] != other[i] :
            diff +=1

    if diff == 1 or diff == 2 :
        return True
    
    return False

def solution(numbers):
    answer = []
    for i in numbers :
        value = bin(i)[2:]
        number = i
        while True :
            number +=1
            other = bin(number)[2:]
            if compare(value, other) :
                break
        answer.append(int(other, 2))

    return answer


# 채점 결과
# 정확성: 81.8
# 합계: 81.8 / 100.0
# => 시간초과로 실패

def compare1(value, other) :
    result = bin(value^other)

    diff = result.count('1')
    if diff == 1 or diff == 2 :
        return True
    
    return False

def solution1(numbers):
    answer = []
    for i in numbers :
        number = i
        while True :
            number +=1
            if compare1(i, number) :
                break
        answer.append(number)

    return answer



def compare1(value, other) :
    result = bin(value^other)

    diff = result.count('1')
    if diff == 1 or diff == 2 :
        return True
    
    return False

def solution1(numbers):
    answer = []
    for i in numbers :
        if i%2 == 0 :
            number = i+1
        else :
            number = i
            while True :
                number +=1
                if compare1(i, number) :
                    break
        answer.append(number)

    return answer

print(solution1([2, 7]))