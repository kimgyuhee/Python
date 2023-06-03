"""
운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 
이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 
우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 
몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 
해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.
"""

from collections import deque

# 배열 중에서 큰 수 찾는 함수
def find_max(arr, value) :
    for a in arr :
        if value < a :
            return True
    return False

# 둘의 코드 합치기
def solution(priorities, location):
    print("실행되고 있나요?")
    p = deque(priorities)
    result = []
    index = 0
    while p:
        index +=1
        print("계속 반복하나요?")
        value = p.popleft()
        print(p, value)
        if find_max(p, value) :
            print("큰 수가 존재합니다. 다시 넣어주세요 !")
            p.append(value)
        else :
            result.append(value)
            print("큰수가 존재하지 않습니다.")
        
    return result

def solution(priorities, location):
    answer = 0
    check = [False for _ in priorities]
    store = deque([])
    for i, p in enumerate(priorities) :
        if location == i :
            find = chr(65+i)
        store.append([chr(65+i), p])
    print(find)
    print(check)
    print(store)
    return answer

def solution(priorities, location):
    print("실행되고 있나요?")
    p = deque(priorities)
    store = deque([])

    for i in range(len(priorities)) :
        store.append(chr(65+i))

    print(p)
    print(store)
    result = []
    process_result = []
    while p :
        print("계속 반복하나요?")
        value = p.popleft()
        process_value = store.popleft()
        print(p, value)
        if find_max(p, value) :
            print("큰 수가 존재합니다. 다시 넣어주세요 !")
            p.append(value)
            store.append(process_value)
        else :
            result.append(value)
            process_result.append(process_value)
            print("큰수가 존재하지 않습니다.")
        
    print(process_result)
    print(result)

    answer = process_result.index(chr(65+location))
    return answer + 1





def solution(priorities, location):
    p = deque(priorities)
    store = deque([])

    for i in range(len(priorities)) :
        store.append(chr(65+i))

    result = []
    process_result = []

    while p :
        value = p.popleft()
        process_value = store.popleft()
        if find_max(p, value) :
            p.append(value)
            store.append(process_value)
        else :
            result.append(value)
            process_result.append(process_value)

    answer = process_result.index(chr(65+location))
    return answer + 1

# 다른 사람 풀이 1
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer



print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))