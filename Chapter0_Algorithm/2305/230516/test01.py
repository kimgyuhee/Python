"""
정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다. 
slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.

n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.
"""

def solution(n, slicer, num_list):
    if n == 1 :
        return num_list[:slicer[1]+1]
    elif n == 2 :
        return num_list[slicer[0]:]
    elif n == 3 :
        return num_list[slicer[0]:slicer[1]+1]
    else :
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]
    
print(solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk를 만드려고 합니다.

변수 i를 만들어 초기값을 0으로 설정한 후 i가 arr의 길이보다 작으면 다음 작업을 반복합니다.

만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
위 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성해 주세요.
"""
def solution(arr):
    stk = []
    i = 0
    while i != len(arr) :
        if len(stk) == 0 :
            stk.append(arr[i])
            i+=1
        elif len(stk)!=0 and stk[-1] < arr[i] :
            stk.append(arr[i])
            i+=1
        elif len(stk)!=0 and stk[-1] >= arr[i] :
            stk.pop()

    return stk

# 다른 사람 풀이
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk

print(solution([1, 4, 2, 5, 3]))