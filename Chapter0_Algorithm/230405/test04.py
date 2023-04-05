import random
import sys
#recursionlimit을 지정해 주지않으면 런타임 에러가 뜨는 까다로운 프로그래머스...
sys.setrecursionlimit(1000000000)
def solution(n, v, A, B, C):

    # 최소값만 곱했을 때 주어진 부피보다 크면 -1 반환
    multiply = min(A)*min(B)*min(C)
    if multiply > v :
        return -1

    # 그 외의 경우는 주어진 부피 이하의 가장 근접한 값을 찾는다
    result = [] # 각 곱의 부피를 저장할 변수
    for i in range(n) : # 가로 [A]
        for j in range(n) : # 세로 [B]
            for k in range(n) : # 깊이 [C]
                value = A[i]*B[j]*C[k]
                result.append(value)

    result = set(result) # 값의 중복을 제거
    answer = list(result) # 중복제거후 set -> list 형 변환
    print(answer)
    if v in answer : # 각 곱의 부피중 주어진 부피가 존재한다면
        return v # 주어진 부피 값 반환
    else : # 존재하지 않는다면
        answer.append(v) # 주어진 부피를 answer에 대입한 후
        answer.sort() # 오름차순으로 정렬해준다.
        findIndex = answer.index(v) # 주어진 부피의 인덱스를 찾은 후
        if findIndex == 0 : # 찾은 인덱스가 0이라면
            return answer[findIndex] # 첫번째 값을 리턴
        return answer[findIndex-1] # 0이 아니라면 전의 가장 가까운 값을 리턴
    

print(solution(3, 101, [1,2,3], [4,5,6], [10,11, 12])) #100
print(solution(4, 101, [1,2,3,4], [4, 5,6,7], [10,11,12,13])) #100
print(solution(4, 100, [1,2,3,4], [4, 5,6,7], [10,11,12,13])) #100
print(solution(3, 2, [1,2,3], [4, 5,6], [10,11, 12])) # -1
print(solution(3, 40, [1,2,3], [4, 5,6], [10,11, 12])) # -1
print(solution(1, 11, [3], [4], [1])) # -1
# A = [random.randrange(1,3000) for _ in range(1000)]
# B = [random.randrange(1,3000) for _ in range(1000)]
# C = [random.randrange(1,3000) for _ in range(1000)]
# A.sort()
# B.sort()
# C.sort()
# print(A)
# print(B)
# print(C)
# print(solution(1000, 10000000, A, B, C)) # -1
# print("출력이 되고 있나요?")