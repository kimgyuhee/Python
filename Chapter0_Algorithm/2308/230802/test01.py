"""
2 * n 타일
가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 
이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 
타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

타일을 가로로 배치 하는 경우
타일을 세로로 배치 하는 경우
예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 
이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.
1 -> 1      [1]
2 -> 1 1, 2 [2]
3 -> 1 1 1, 1 2, 2 1 [3]
4 -> [5]
5 -> [8]

1 1 1 1 1 1 -> 1
1 1 1 1 2 -> 5
1 1 2 2
1 2 2 1
2 2 1 1 
1 2 1 2
2 1 2 1
2 1 1 2
2 2 2 -> 1
"""
from itertools import combinations

def fibo(n) :
    answer1 = 1
    answer2 = 2
    if n == 1 :
        return answer1
    elif n == 2 :
        return answer2
    else :
        for i in range(n-2) :
            temp = answer1
            answer1 = answer2
            answer2 = answer1 + temp
    answer = answer2%1000000007
    return answer

def solution(n):
    answer = fibo(n)
    return answer

# 다른 사람 풀이
def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b

for i in range(1, 100) :
    print(i, solution(i))
