"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여
F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어
F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수,
solution을 완성해 주세요.
"""

def solution(n):
    answer = [0, 1]

    for i in range(2, n+1) :
        answer.append(answer[i-2]+answer[i-1])

    print(answer)


    return answer[n]%1234567

print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(4))
print(solution(1000))

print("=========")
for i in range(0) :
    print(i)
print("=========")
for i in range(2,2) :
    print(i)