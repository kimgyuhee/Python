"""
정수 n, left, right가 주어집니다. 
다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

>>> 입출력 예시
n   left	right	result
3	2	    5	    [3,2,2,3]
4	7	    14	    [4,3,3,3,4,4,4,4]

"""

def solution(n, left, right):
    answer = [[n+1]*n for _ in range(n)]
    for i in range(n) :
        print(answer)
        for j in range(i+1) :
            for k in range(j+1) :
                print(j, k)
                if j != k :
                    answer[k][i] -=1
                answer[j][k] -=1
    return answer

# 대실패 다시 하기 문제 이해 못함
def solution(n, left, right):
    result = []
    answer = [[n+1]*n for _ in range(n)]
    finish = False
    for i in range(n) :
        if finish :
            break
        print(answer)
        for j in range(i+1) :
            if finish :
                break
            for k in range(j+1) :
                if i == n-1 :
                    finish = True
                    break
                if j != k :
                    answer[k][i] -=1
                answer[j][k] -=1
    
    for a in answer :
        for value in a :
            result.append(value-1)

    return result[left:right+1]


"""
채점 결과
정확성: 15.0
합계: 15.0 / 100.0
>>> 시간초과
"""
import itertools

def solution(n, left, right):
    answer = [[n+1]*n for _ in range(n)]
    for i in range(n) :
        arr = [i for i in range(n-i)]
        per = list(itertools.product(arr, repeat=2))
        for p in per :
            answer[p[0]][p[1]] -=1

    result = []
    for a in answer :
        result+=a
    return result[left:right+1]


"""
채점 결과
정확성: 35.0
합계: 35.0 / 100.0
>>> 시간초과
"""
def solution(n, left, right):
    answer = [[i+1 for i in range(n)]]
    result = []
    num = 0
    for i in range(n) :
        value = answer[i]
        for n in range(num) :
            value[n] +=1
        result +=value
        num+=1
        answer.append(value)
    return result[left:right+1]

"""
채점 결과
정확성: 45.0
합계: 45.0 / 100.0
>>> 시간초과
"""

def solution(n, left, right):
    answer = [i+1 for i in range(n)]
    result = []
    for i in range(n) :
        value = (i*[answer[i]]) + answer[i:]
        result +=value

    return result[left:right+1]

"""
좌측엔 좌표, 오른쪽엔 해당 좌표에 실제로 있어야하는 값을 의미한다. 규칙을 보면 알겠지만 두 좌표 중에서
0과 0밖에 없다면 1
1이 하나라도 있다면 2
2가 하나라도 있다면 3이 되는 것을 확인할 수 있다.

>>> 배열의 규칙
>>> 2차원 배열 N * N 일때
>>> array[i][j] i는 몫, j는 나머지 부분
"""
def solution(n, left, right):
    answer = []
    for number in range(left, right+1):
        quotient, remainder = divmod(number, n)
        answer.append(quotient + 1 if quotient > remainder else remainder + 1)
    return answer


# 다른 사람 풀이 1 
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))

l = [1, 2, 3, 4]
