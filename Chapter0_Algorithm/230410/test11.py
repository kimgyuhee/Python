"""
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.
"""

def solution(sides):
    """
    4, 5, 7, 8, 9

    5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20
    """
    def findMax(a, b) :
        if a > b :
            return a, b
        else :
            return b, a
    answer = 0
    maxV, minV = findMax(sides[0], sides[1])

    for i in range(maxV-minV ,maxV) :
        # print(i)
        answer +=1

    for i in range(maxV+1, maxV+minV) :
        answer +=1

    return answer

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))
