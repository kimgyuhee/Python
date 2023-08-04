from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_truck = list(truck_weights)
    on_truck = [0] * bridge_length
    trucks = 0
    while len(on_truck) :
        answer +=1
        trucks -= on_truck.pop(0)
        if wait_truck :
            if trucks + wait_truck[0] <= weight :
                trucks +=wait_truck[0]
                on_truck.append(wait_truck.pop(0))
            else :
                on_truck.append(0)

    return answer


def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait_truck = deque(truck_weights)
    on_truck = [0] * bridge_length
    trucks = 0
    while len(on_truck) :
        answer +=1
        trucks -= on_truck.pop(0)
        if wait_truck :
            if trucks + wait_truck[0] <= weight :
                trucks +=wait_truck[0]
                on_truck.append(wait_truck.popleft())
            else :
                on_truck.append(0)

    return answer


# 다른 사람 풀이
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    print(bridge)
    trucks = collections.deque(w for w in truck_weights)

    for i in range(bridge_length):
        print(f"{i+1}번째 실행중")
        bridge.push(DUMMY_TRUCK)
        print(bridge)
        print("====================")


    count = 0
    while trucks: # 트럭이 다 올라갔다 !!!!
        bridge.pop()
        print(bridge)

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    print("또 다른 반복문")
    print(bridge)

    while bridge:
        print(bridge)
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()



# 다른 사람 풀이 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()
    """
    truck_weights를 reverse 한 이유는 정배열에서 pop(0)을 써서 넣고 빼는게 시간이 걸리니, 
    dequeue를 만드는 대신 아예 순서를 뒤집어서 pop()으로 해결한 듯 합니다.
    """
    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step

print(solution(10, 12, [4,4,4,2,2,1,1,1,1]))
# print(solution())