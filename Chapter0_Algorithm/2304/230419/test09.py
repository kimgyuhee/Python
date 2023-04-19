"""
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
"""

def solution(arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2) :
        value = []
        for a, b in zip(ar1, ar2) :
            value.append(a+b)
        answer.append(value)
    return answer

def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(arr1,arr2)]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))