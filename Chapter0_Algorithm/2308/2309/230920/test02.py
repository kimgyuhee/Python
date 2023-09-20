
from collections import deque
def solution(order):
    container_belt = deque([i+1 for i in range(len(order))]) # 1부터 n까지 정렬된 택배
    sub_container_belt = [] # 잠시 보관해 두는 택배
    truck = [] # 트럭에 실린 택배

    for i in range(len(order)) :
        value = order[i]

        if len(container_belt) == 0 :
            if value == sub_container_belt[len(sub_container_belt)-1] :
                truck.append(value)
                sub_container_belt.remove(value)
            else :
                break
            
        elif container_belt[0] < value :
            for i in range(container_belt.index(value)) :
                v = container_belt.popleft()
                sub_container_belt.append(v)
            truck.append(value)
            container_belt.popleft()
        elif container_belt[0] > value : 
            if value == sub_container_belt[len(sub_container_belt)-1] :
                truck.append(value)
                sub_container_belt.remove(value)
            else :
                break

        else : # container_belt[0] == value
            truck.append(value)
            container_belt.popleft()

    answer = len(truck)
    return answer

print(solution( [3, 5, 4, 2, 1] ))