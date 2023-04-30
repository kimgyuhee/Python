"""
정수 배열 numbers와 정수 n이 매개변수로 주어집니다. 
numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(numbers, n):
    answer = 0

    for i in numbers :
        # print(i, answer)
        if n < answer :
            break
        answer +=i

    return answer

print(solution([34, 5, 71, 29, 100, 34], 123))

# 동일한 변수 이름 써서 에러가 자꾸 났음

def solution(numbers, n):
    answer = 0
    i=0
    while answer<=n:
        answer+=numbers[i]
        i+=1
    return answer


"""
'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 
문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
"""
def solution(rny_string):
    answer = rny_string.replace("m", "rn")
    return answer

"""
양의 정수 n이 매개변수로 주어질 때, 
n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(n):
    answer = 0
    if n%2 == 1 :
        for i in range(1,n+1,2):
            answer +=i
    else :
        for i in range(0,n+1,2):
            answer +=(i**2)
    return answer

def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)