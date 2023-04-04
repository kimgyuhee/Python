"""
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(numbers, direction):
    answer = []
    if direction == "right" :
        answer.append(numbers[len(numbers)-1])
        answer.extend(numbers[:-1])
    elif direction == "left" :
        answer = numbers[1:]
        answer.append(numbers[0])
    else :
        print("방향 명령어가 잘못되었습니다. ")
    return answer


from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
print(solution([1, 2, 3], "right"))