"""
도둑이 어느 마을을 털 계획을 하고 있습니다. 
이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.
각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 
도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.
"""
# https://school.programmers.co.kr/questions/46813

def solution(money):
    # 두 수를 비교해서 큰 값을 리턴하는 함수
    def maxValue(c1, c2) :
        if c1 < c2 :
            return c2
        else :
            return c1
    
    def listReverse(l) :
        if l[0] <= l[len(l)-1] :
            l.reverse()
        return l
    answer = 0 # 정답을 담을 변수
    # 경우가 2가지 밖에 나오지 않음
    case1 = 0 # 도둑이 훔칠 수 있는 돈의 합을 저장할 변수1
    case2 = 0 # 도둑이 훔칠 수 있는 돈의 합을 저장할 변수2

    if len(money)%2 == 0 : # 집이 짝수개 일때
        for m in range(len(money)) :
            if m%2 == 0 : # 찻번째 집부터 훔칠때
                case2 +=money[m]
            else :  # 두번째 집부터 훔칠때
                case1 +=money[m]
    else : #집이 홀수개 일때
        money = listReverse(money)
        for m in range(len(money)-1) :
            if m%2 == 0 : # 첫번째 집부터 훔칠때
                case2 +=money[m]
            else : # 두번째 집부터 훔칠때
                case1 +=money[m]

    answer = maxValue(case1, case2)
    return answer


print(solution([1, 2, 3, 1]))
print(solution([1, 7, 2, 4]))
print(solution([1, 2, 3, 1, 5, 3, 2, 1, 0]))
print(solution([1, 1, 4, 1, 4]))
print(solution([0, 1, 4, 1, 10]))
print(solution([14, 0, 5, 0, 10]))

print("{0:=^20}".format("나 진짜로 운다요..."))

l = [1]
if l[0] <= l[len(l)-1] :
    l.reverse()
    print(l)
    print("바뀔까??????")


print("{0:=^20}".format("구글링 했지만 내 코드도 맞는것 같은데...."))
def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대

print(solution([1, 2, 3, 1]))
print(solution([1, 7, 2, 4]))
print(solution([1, 2, 3, 1, 5, 3, 2, 1, 0]))
print(solution([1, 1, 4, 1, 4]))
print(solution([0, 1, 4, 1, 10]))
print(solution([14, 0, 5, 0, 10]))


print("{0:=^30}".format(" 이분은 뭐지...... 엄청나다... "))
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)

print(solution([1, 2, 3, 1]))
print(solution([1, 7, 2, 4]))
print(solution([1, 2, 3, 1, 5, 3, 2, 1, 0]))
print(solution([1, 1, 4, 1, 4]))
print(solution([0, 3, 6]))
print(solution([14, 0, 5, 0, 10]))