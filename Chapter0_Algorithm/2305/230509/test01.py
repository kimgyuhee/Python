"""
1937년 Collatz란 사람에 의해 제기된 이 추측은, 
주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 
작업은 다음과 같습니다.


예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 
위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 
단, 주어진 수가 1인 경우에는 0을, 
작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.
"""

def solution(num):
    answer = 0
    while answer !=500 :
        if num == 1 :
            break
        else :
            if num%2 == 0 :
                num = num//2
            else :
                num = num*3+1
            answer+=1

    if answer >= 500 :
        return -1
    return answer

print(solution(6))
print(solution(16))
print(solution(1))
print(solution(626331))
print(solution(1262631))

"""
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, 
solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
"""

def solution(arr, divisor):
    answer = []
    for a in arr :
        if a%divisor == 0 :
            answer.append(a)

    if answer == [] :
        return [-1]
    
    return sorted(answer)


