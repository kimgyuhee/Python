"""
정수 배열 arr가 주어집니다. 
이때 arr의 원소는 1 또는 0입니다. 
정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 
solution 함수를 완성해 주세요.

단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.
"""

def solution(arr, idx):
    if 1 not in arr[idx:] :
        return -1
    else :
        return arr[idx:].index(1)+idx

# 다른 사람 풀이
# index의 두번쨰 인자는 시작인덱스를 의미한다.
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer

"""
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 
각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 
매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 
순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(todo_list, finished):
    answer = []
    for todo, result in zip(todo_list, finished) :
        if not result :
            answer.append(todo)
    return answer

# 다른 사람 풀이
def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]


"""
정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 
각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 
그 사이의 값을 모두 포함하는 구간을 의미합니다.

이때 배열 arr의 첫 번째 구간에 해당하는 배열과 
두 번째 구간에 해당하는 배열을 앞뒤로 붙여 
새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr, intervals):
    answer = arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]
    return answer

"""
음이 아닌 정수를 9로 나눈 나머지는 
그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 
이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.
"""

def solution(number):
    answer = list(map(int, list(number)))
    print(answer)
    return sum(answer)%9


def solution(number):
    return sum(list(map(int, number))) % 9

print(solution("123"))

