from collections import deque
def solution(bridge_length, weight, truck_weights):
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
                if len(on_truck) == bridge_length :
                    pass_truck.append(on_truck.popleft())
            else :
                wait_truck.appendleft(truck)
                break

        print("대기중인 트럭",wait_truck)
        print("도로에 있는 트럭", on_truck)
        print("경과 시간 : ", time)
        print()
        while len(on_truck) :
            pass_truck.append(on_truck.popleft())


    return time
# print(solution(2, 10, [1, 1, 1, 1, 1, 1]))
# print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))
print(solution(10, 10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(solution(10, 12, [4,4,4,2,2,1,1,1,1]))
print(solution(10, 12, [1,1,1,1,2,2,4,4,4]))

"""
1   []              [1]         [1, 1, 1, 1, 1]
2   []              [1, 1]      [1, 1, 1, 1]
3   [1]             [1, 1]      [1, 1, 1]
4   [1, 1]          [1, 1]      [1, 1]
5   [1, 1, 1]       [1, 1]      [1]
6   [1, 1, 1, 1]    [1, 1]      []
7   [1, 1, 1, 1, 1] [1]         []
8   [1, 1, 1, 1, 1, 1]          []
"""


# 다른 사람 풀이
def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) # 트럭 무게
    x = [0] * bridge_length # 다리
    s=0
    while (x):
        time += 1
        print(s, end = " => ")
        s-=x.pop(0) # s: 다리 위의 총 트럭 무게
        print(s)
        print(x)
        print(p)
        if p:
            if ( s + p[0] ) <= weight:
                s+=p[0] # 여유되면 트럭 추가
                x.append(p.pop(0)) # 다리에 트럭 추가  
            else:
                x.append(0) # 여유 없으면 무게 0 추가

    return time


print(solution(10, 12, [4,4,4,2,2,1,1,1,1]))