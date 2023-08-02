# 채점 결과
# 정확성: 28.6
# 합계: 28.6 / 100.0

from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 1
    pass_truck = [] # 다리를 통과한 트럭을 저장할 리스트
    wait_truck = deque(truck_weights) # 대기하고 있는 트럭 리스트
    on_truck = deque([])  # 다리 위에 있는 트럭

    while pass_truck != truck_weights : # 통과된 트럭과 처음 기다렸던 트럭 리스트가 같을 때까지 반복문 실행
        truck1 = wait_truck.popleft()
        on_truck.append(truck1)
        time += bridge_length # 트럭이 한번 지나가려면 다리의 길이만큼 지나가야 한다.
        while len(wait_truck) : # 도로에 올라갈 수 있는 트럭의 수와 무게를 계산하기 위한 반복문

            if len(on_truck) >= bridge_length : # 반복문 종료 조건
                break

            truck = wait_truck.popleft()
            if truck + sum(on_truck) <= weight : # 무게가 적합할 경우
                on_truck.append(truck)
                time +=1 # 다리의 길이가 추가되는 것이 아니라 +1 초만 초과한다.
            else : # 적합하지 않은 경우 로도에 트럭을 추가하는 것을 종료한다.
                wait_truck.appendleft(truck)
                break

        while len(on_truck) :
            pass_truck.append(on_truck.popleft())


    return time

print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))
print(solution(10, 10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(solution(10, 12, [4,4,4,2,2,1,1,1,1]))
print(solution(10, 12, [1,1,1,1,2,2,4,4,4]))