"""
영재는 택배상자를 트럭에 싣는 일을 합니다. 
영재가 실어야 하는 택배상자는 크기가 모두 같으며 
1번 상자부터 n번 상자까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 영재에게 전달됩니다. 
컨테이너 벨트는 한 방향으로만 진행이 가능해서 벨트에 놓인 순서대로(1번 상자부터) 상자를 내릴 수 있습니다. 
하지만 컨테이너 벨트에 놓인 순서대로 택배상자를 내려 바로 트럭에 싣게 되면 
택배 기사님이 배달하는 순서와 택배상자가 실려 있는 순서가 맞지 않아 배달에 차질이 생깁니다. 
따라서 택배 기사님이 미리 알려준 순서에 맞게 영재가 택배상자를 실어야 합니다.

만약 컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면 
그 상자를 트럭에 실을 순서가 될 때까지 잠시 다른 곳에 보관해야 합니다. 
하지만 고객의 물건을 함부로 땅에 둘 수 없어 보조 컨테이너 벨트를 추가로 설치하였습니다. 
보조 컨테이너 벨트는 앞 뒤로 이동이 가능하지만 입구 외에 다른 면이 막혀 있어서 맨 앞의 상자만 뺄 수 있습니다(즉, 가장 마지막에 보조 컨테이너 벨트에 보관한 상자부터 꺼내게 됩니다). 
보조 컨테이너 벨트를 이용해도 기사님이 원하는 순서대로 상자를 싣지 못 한다면, 더 이상 상자를 싣지 않습니다.

예를 들어, 영재가 5개의 상자를 실어야 하며, 택배 기사님이 알려준 순서가 기존의 컨테이너 벨트에 네 번째, 세 번째, 첫 번째, 두 번째, 다섯 번째 놓인 택배상자 순서인 경우, 
영재는 우선 첫 번째, 두 번째, 세 번째 상자를 보조 컨테이너 벨트에 보관합니다. 
그 후 네 번째 상자를 트럭에 싣고 보조 컨테이너 벨트에서 세 번째 상자 빼서 트럭에싣습니다. 
다음으로 첫 번째 상자를 실어야 하지만 보조 컨테이너 벨트에서는 두 번째 상자를, 
기존의 컨테이너 벨트에는 다섯 번째 상자를 꺼낼 수 있기 때문에 더이상의 상자는 실을 수 없습니다. 
따라서 트럭에는 2개의 상자만 실리게 됩니다.

택배 기사님이 원하는 상자 순서를 나타내는 정수 배열 order가 주어졌을 때, 
영재가 몇 개의 상자를 실을 수 있는지 return 하는 solution 함수를 완성하세요.

"""

from collections import deque

def solution(order):
    container_belt = deque([i+1 for i in range(len(order))])
    sub_container_belt = []
    truck = []
    print(order, container_belt, sub_container_belt, truck)
    for i in range(len(order)) :
        value = order[i]
        if container_belt[0] < value :
            print(f"{container_belt[0]} < {value}")
            print(container_belt.index(value))
            for i in range(container_belt.index(value)) :
                v = container_belt.popleft()
                sub_container_belt.append(v)
            truck.append(value)
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



def solution(order):
    move_count = 0 # 2 6 3 4
    container_belt = deque([i+1 for i in range(len(order))]) # 1, 2, 3, 4, 5, 6
    sub_container_belt = [] # 1
    truck = [] # 2
    for i in range(len(order)) :
        value = order[i]
        if len(truck) == 0 :
            truck.append(value)
            for i in range(value) :
                v = container_belt.popleft()
                sub_container_belt.append(v)
        else :
            if container_belt[0] > value :
                for i in range(container_belt.index(value)) :
                    v = container_belt.popleft()
                    sub_container_belt.append(v)
                truck.append(value)
            else :
                if value == sub_container_belt[len(sub_container_belt)-1] :
                    truck.append(value)
                    sub_container_belt.remove(value)
                else :
                    break


    answer = len(truck)
    return answer


# 채점 결과
# 정확성: 50.0
# 합계: 50.0 / 100.0

def solution(order):
    container_belt = deque([i+1 for i in range(len(order))]) # 1, 2, 3, 4, 5, 6
    sub_container_belt = [] # 1
    truck = [] # 2
    print(order, container_belt, sub_container_belt, truck)
    for i in range(len(order)) :
        value = order[i]
        print(f"{value}번째 택배 상자를 넣어보아요 ~")
        if len(container_belt) == 0 :
            if value == sub_container_belt[len(sub_container_belt)-1] :
                truck.append(value)
                sub_container_belt.remove(value)
                #print("\n 두번째 조건문에 들어왔어요", container_belt, sub_container_belt, truck)
            else :
                print("나 종료합니다")
                break
            
        elif container_belt[0] < value :
            print(f"{container_belt[0]} < {value}")
            print(container_belt.index(value))
            for i in range(container_belt.index(value)) :
                v = container_belt.popleft()
                sub_container_belt.append(v)
            truck.append(value)
            container_belt.popleft()
            print("\n 첫번쨰 조건문에 들어왔어요 ~", container_belt, sub_container_belt, truck)
        elif container_belt[0] > value : 
            if value == sub_container_belt[len(sub_container_belt)-1] :
                truck.append(value)
                sub_container_belt.remove(value)
                print("\n 두번째 조건문에 들어왔어요", container_belt, sub_container_belt, truck)
            else :
                print("나 종료합니다")
                break

        else : # container_belt[0] == value
            truck.append(value)
            container_belt.popleft()
            print("\n 세번쨰 조건문에 들어왔어요 ", container_belt, sub_container_belt, truck)
            

    print(">>>", order, container_belt, sub_container_belt, truck)
    answer = len(truck)
    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
print(solution([1, 2, 3, 4, 5]))
print(solution([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]))
print(solution([3, 2, 1, 4, 5]))
print(solution([1, 2, 10, 5, 6, 7, 3, 4, 9, 8]))