"""
성준이는 마당에 땅을 파서 야외수영장을 설치하려 한다.

그런데, 성준이의 마당은 지질학적인 문제로 파낼 수 있는 가로 길이, 세로 길이, 깊이가 각각 n개의 정수 중 하나로 정해져있다. (예시 참고)

예를 들어, n=3이고, 야외수영장의 가로 길이는 1, 2, 3 중 하나여야 하고, 
세로 길이는 4, 5, 6 중 하나여야 하고, 
깊이는 10, 11, 15 중 하나여야 한다.

또한, 수영장의 부피는 v 이하여야 한다.

이러한 제약을 지키면서, 성준이는 수영장의 부피가 최대가 되도록 하고 싶어한다.

n, v, 가로 길이 후보, 세로 길이 후보, 깊이 후보가 주어질 때, 수영장의 최대 부피를 구해보자.

"""

def solution(n, v, A, B, C):
    
    # 최소값만 곱했을 때 v 보다 크다면 -1리턴
    multiply = min(A)*min(B)*min(C)
    if multiply > v :
        return -1
    
    result = []
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                value = A[i]*B[j]*C[k]
                result.append(value)

    result = set(result) # 중복제거
    answer = list(result)

    if v in answer :
        return v 
    else :
        answer.append(v)
        answer.sort()
        findIndex = answer.index(v)
        if findIndex == 0 :
            return answer[findIndex]
        return answer[findIndex-1]

# print(solution(3, 101, [1,2,3], [4,5,6], [10,11, 12])) #100
# print(solution(4, 101, [1,2,3,4], [4, 5,6,7], [10,11,12,13])) #100
# print(solution(3, 2, [1,2,3], [4, 5,6], [10,11, 12])) # -1
print(solution(3, 40, [1,2,3], [4, 5,6], [10,11, 12])) # -1