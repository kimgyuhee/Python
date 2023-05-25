"""
정수 배열 arr와 query가 주어집니다.

query를 순회하면서 다음 작업을 반복합니다.

짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 
배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 
배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.

"""

def solution(arr, query):
    answer = []
    for i in range(len(query)) :
        value = query[i]
        if i%2 == 0 :
            arr = arr[:value+1]
        else :
            arr = arr[value:]
    return arr


# 다른 사람 풀이
def solution(arr, query):
    for k, q in enumerate(query):
        if k % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    return arr


print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))