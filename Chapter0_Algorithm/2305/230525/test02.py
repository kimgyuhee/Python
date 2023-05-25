"""
양의 정수 n이 매개변수로 주어집니다. 
n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 
시계방향 나선형으로 배치한 이차원 배열을 
return 하는 solution 함수를 작성해 주세요.

오른쪽 -> 아래 -> 왼쪽 -> 위쪽 -> 오른쪽 -> 아래쪽

(+)     (-)
오른쪽, 왼쪽 행 고정
1, 1    1, -1
아래쪽, 위쪽 열 고정
-1, 1   -1, -1
"""
def solution(n):
    answer = [[0]*n for _ in range(n)]
    num = 1
    switch = [1, 1]
    RL = n      # 오른쪽, 왼쪽 횟수
    DT = n-1    # 아래쪽, 위쪽 횟수
#    while RL != 0 and DT != 0 :
#        print("" , end = " ")
                  
    return answer

print(solution(4))
    
#result = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
#for r in result :
#    print(r)

n = 3
while n != 0 :
    for i in range(n) :
        print("*"*n)
    n-=1