# 효율적인 화폐 구성
N = 3
M = 7
k = [2, 3, 5]

def solution(N, M, k) :

    # 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [10001] * (M+1)

    # 다이나믹 프로그래밍 진행(보텀업)
    d[0] = 0
    for i in range(N) :
        for j in range(k[i], M+1):
            if d[j - k[i]] != 10001  : # (i - k) 원을 만드는 방법이 존재하는 경우
                d[j] = min(d[j], d[j-k[i]] + 1)

    if d[M] == 10001 :
        print(-1)
    else :
        print(d[M])

solution(2, 3, [2, 3])
solution(3, 15, [2, 3, 5])
solution(1, 7, [5])