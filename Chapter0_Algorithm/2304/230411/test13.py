"""
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 
연속된 수 num개를 더한 값이 total이 될 때, 
정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
"""

def solution(num, total):
    answer = []
    value = total//num
    for i in range((num-1)//2) :
        answer.append(value-(i+1))
    for i in range(num//2+1) :
        answer.append(value+i)

    return sorted(answer)


# 다른 사람 풀이 방법1
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]


# 다른 사람 풀이 방법2
def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    print(diff, var)
    start_num = diff//num
    print(start_num)
    answer = [i+1+start_num for i in range(num)]
    return answer


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))
