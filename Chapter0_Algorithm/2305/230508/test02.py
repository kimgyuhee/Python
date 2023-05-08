"""
2차원 정수 배열 board와 정수 k가 주어집니다.

i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 
return 하는 solution 함수를 완성해 주세요.
"""

# 문제 잘못이해함
def solution(board, k):
    answer = 0
    for b in board :
        for n in b :
            if n <= k :
                answer+=n
    return answer

def solution(board, k):
    answer = 0
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if i+j <= k :
                answer+=board[i][j]
    return answer


# 다른 사람 풀이
def solution(board, k):
    return sum(board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i + j <= k)


print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))

"""
정수 배열 arr가 주어집니다. 
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 
50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때, 
arr(x) = arr(x + 1)인 x가 항상 존재합니다. 
이러한 x 중 가장 작은 값을 return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 
같은 인덱스의 원소가 각각 서로 같음을 의미합니다.
"""

def solution(arr):
    answer = [[], arr]
    idx = 0

    while answer[idx] != answer[idx+1] :
        after = arr.copy()
        # 규칙에 따라 변화되는 리스트
        for i in range(len(arr)) :
            if after[i] >= 50 and after[i]%2 == 0 :
                after[i] = after[i]//2
            elif after[i] < 50 and after[i]%2 == 1 :
                after[i] = after[i]*2+1
        answer.append(after)
        print(idx, answer)
        idx +=1
        arr = after

    return idx+1

print(solution([1, 2, 3, 100, 99, 98]))