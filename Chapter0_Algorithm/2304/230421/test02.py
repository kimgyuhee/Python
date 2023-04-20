"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, 
solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
"""

# 합계: 56.3 / 100.0
# 시간 초과 코드
def checksosu(n) :
    count = 0
    for i in range(1, n+1) :
        if n%i == 0 :
            count +=1
    return count

# 조금 더 효울적인 약수 구하기
def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(n):
    answer = 0
    for num in range(2, n+1) :
        if len(getMyDivisor(num)) == 2 :
            answer +=1
    return answer

# 합계: 68.8 / 100.0
# 시간 초과
def solution(n):
    answer = 0

    for num in range(2, n+1) :
        divisorsList = []

        for i in range(1, int(num**(1/2)) + 1):
            if (num % i == 0):
                divisorsList.append(i) 
                if ( (i**2) != num) : 
                    divisorsList.append(num // i)

        if len(divisorsList) == 2 :
            answer +=1
    return answer

"""
에라토스테너스의 체
수학에서 에라토스테네스의 체는 소수를 찾는 방법이다. 
고대 그리스 수학자 에라토스테네스가 발견하였다.

2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 
그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
자기 자신을 제외한 2의 배수를 모두 지운다.
남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
자기 자신을 제외한 3의 배수를 모두 지운다.
남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
자기 자신을 제외한 5의 배수를 모두 지운다.
남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
자기 자신을 제외한 7의 배수를 모두 지운다.
위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
"""
# 다른 사람 풀이 1
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


# 다른 사람 풀이 2
def solution(n):
    answer = 0
    for i in range(2, n+1):
        if i == 2:
            answer += 1
            continue
        for j in range(2, int(i ** (1/2)) + 1):
            if i % j == 0:
                answer -= 1
                break
        answer += 1
    return answer

print(solution(10))