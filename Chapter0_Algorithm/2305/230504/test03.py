"""
최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때, 
앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 
return하도록 solution 함수를 완성해주세요. 마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.
"""

def solution(names):
    answer = []
    for i in range(0, len(names), 5) :
        answer.append(names[i])
    return answer

# 다른 사람 풀이
def solution(names):
    return names[::5]


"""
정수 n이 매개변수로 주어질 때, 
다음과 같은 n × n 크기의 이차원 배열 arr를 
return 하는 solution 함수를 작성해 주세요.

arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
"""

def solution(n):
    answer = [[0]*n for _ in range(n)]
    count =0
    for a in answer :
        a[count] = 1
        count +=1
    return answer

print(solution(3))

# 다른 사람 풀이
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer

