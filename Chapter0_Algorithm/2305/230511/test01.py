"""
정수 배열 arr가 주어집니다. 
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.
"""

def solution(arr):
    answer = []
    if arr.count(2) == 0 :
        return [-1]
    elif arr.count(2) == 1 :
        return [2]
    else :
        front = arr.index(2)
        end = arr[::-1].index(2)
        return arr[front : len(arr)-end]
    

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1]))