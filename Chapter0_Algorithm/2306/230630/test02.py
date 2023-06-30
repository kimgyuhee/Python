"""
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 
다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 
다음과 같이 건너야 합니다.
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 
다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

"""

def solution(bridge_length, weight, truck_weights):
    answer = 0
    if len(truck_weights) == 1 :
        return bridge_length + 1
    
    for i in range(len(truck_weights)-1) :
        if truck_weights[i] + truck_weights[i+1] <= weight :
            answer -=1
        else :
            answer +=bridge_length
    return answer


from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    pass_truck = []
    crossing_truck = []
    now_weight = truck_weights.popleft()
    while truck_weights :
        if len(truck_weights) == 1 :
            answer = answer +bridge_length + 1
        w = truck_weights.popleft()
        now_weight +=w
        if now_weight <= weight :
            answer +=bridge_length
            answer +=1
        else :
            answer +=bridge_length
            now_weight = 0

    return answer


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    pass_truck = []
    crossing_truck = []
    now_wight = truck_weights.popleft()
    possible = True
    now_count = 0
    while len(truck_weights)!=0:
        print(f"현재 지난 초 : {answer}, now_count : {now_count}")
        print(f"대기 중인 트럭 : {truck_weights}")
        print(f"현재 무게 : {now_wight}")
        if now_count == 0 :
            answer +=bridge_length
        else :
            answer +=now_count
            now_count = 0

        w = truck_weights.popleft()
        if now_wight+w <= weight :
            now_wight +=w
            now_count +=1
        else :
            truck_weights.appendleft(w)
            now_wight = 0

    return answer

print(solution(5, 10, [7,4,5,1,6]))
print(solution(2, 10, [7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,	[10,10,10,10,10,10,10,10,10,10]))