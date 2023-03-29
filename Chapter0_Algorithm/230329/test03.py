"""
다이나믹 프로그래밍(동적 계획법)
- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장
- 두가지 방식(탑다운과 보텀업)이 있다

* 동적 ?
- 동적 할당 : 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법
-> 다이나믹 프로그래밍에서 '다이나믹'은 별다른 의미 없이 사용된 단어입니다.

어떨 때 사용할 수 있는가?
1. 최적 부분 구조
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제 답을 모아서 큰 문제를 해결
2. 중복되는 부분 문제
    - 동일한 작은 문제를 반복적으로 해결

점화식이란? 인접한 항들 사이의 관계식
An = A(n-1) + A(n-2), A1 = 1, A2 = 1

메모이제이션 : 다이나믹 프로그래밍을 구현하는 방법 중 하나
- 한 번 계산한 결과를 메모리 공간에 메모하는 기법
- 값을 기록해 놓는다는 점에서 캐싱이라고도 합니다.

탑다운(메모이제이션) 방식은 하향식이라고도 하며 보탐업 방식은 상향식이라고 한다
다이나믹 프로그래밍의 전형적인 형태는 보텀업입니다.
    - 결과 저장용 리스트는 DP 테이블이라고 부릅니다
엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미

* 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복됩니다.
분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않습니다.
"""

s = [2,3,4,5,6,2,7,444,6]
s = s.index(max(s))
print(s)
s = "hello i am david"
print("hello" in s)

print("{0:#^30}".format(" 프로그래밍 시작 "))
def solution(triangle):
    answer = 0
    nowIndex = 0
    def checkComp(triangle, nowIndex , answer) :
        triMax = max(triangle[nowIndex:nowIndex+2])
        answer += triMax
        print(triangle[nowIndex:nowIndex+2])
        print(f"{triangle} 에서 최대값은? index : {nowIndex}인 value : {triMax}")
        nowIndex = triangle.index(triMax)

        return nowIndex, answer
    
    for i in triangle :
        nowIndex, answer = checkComp(i,nowIndex, answer)
        print(nowIndex)
        print(answer)  

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))



# 개미 전사 : 문제 해결 아이디어
def solution1(array):
    # 정수 N 입력받기
    # n = int(input()) 
    # 모든 식량 정보 입력 받기
    # array = list(map(int, input().split()))
    n = len(array)
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 100
    print(d)
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    print(f"d[0] = array[0] -> {d[0]} = {array[0]}")

    print(d) 
    for i in range(2, n) :
        print(f"d[i] : {d[i]}")
        print(f"d[i-1] : {d[i-1]}")
        print(f"d[i-2] : {d[i-2]}")
        print(f"array[i] : {array[i]}")
        print(f"max(d[i-1], d[i-2]) : {max(d[i-1], d[i-2])}")
        d[i] = max(d[i-1], d[i-2] + array[i])
        print(d)
    print(d[n-1])

# print(solution1([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

array = [1, 3, 1, 5, 1, 1, 1, 6, 7, 110]
solution1(array)
solution1([1, 7, 3])