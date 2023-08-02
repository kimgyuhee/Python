"""
다리를 지나는 트럭

문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간   다리를 지난 트럭    다리를 건너는 트럭  대기 트럭
0	      []	          []	         [7,4,5,6]
1~2       []	          [7]	         [4,5,6]
3	      [7]	          [4]	         [5,6]
4	      [7]	          [4,5]	         [6]
5	      [7,4]	          [5]	         [6]
6~7	      [7,4,5]	      [6]	         []
8	      [7,4,5,6]	      []	         []

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.
solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 
다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
"""

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 1
    pass_truck = []
    wait_truck = deque(truck_weights)
    on_truck = deque([])
    while pass_truck != truck_weights :
        truck1 = wait_truck.popleft()
        on_truck.append(truck1)
        time += bridge_length
        print(truck1)
        while len(wait_truck) :
            print("도로위에 있는 트럭 갯수 : ", len(on_truck))
            if len(on_truck) >= bridge_length : # 종료 조건
                break

            truck = wait_truck.popleft()
            print(f"{truck} + {sum(on_truck)} <= {weight} ==> {on_truck}")
            if truck + sum(on_truck) <= weight : # 무게가 적합할 경우
                print("무게 합이 적합합니다.🈴")
                on_truck.append(truck)
                time +=1
            else :
                wait_truck.appendleft(truck)
                break

        print("대기중인 트럭",wait_truck)
        print("도로에 있는 트럭", on_truck)
        print("경과 시간 : ", time)
        print()
        while len(on_truck) :
            pass_truck.append(on_truck.popleft())


    return answer

# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))