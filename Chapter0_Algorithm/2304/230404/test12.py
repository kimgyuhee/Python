"""
"스노우타운"에서 호텔을 운영하고 있는 "스카피"는 호텔에 투숙하려는 고객들에게 방을 배정하려 합니다. 
호텔에는 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다. 
처음에는 모든 방이 비어 있으며 "스카피"는 다음과 같은 규칙에 따라 고객에게 방을 배정하려고 합니다.

1. 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
2. 고객은 투숙하기 원하는 방 번호를 제출합니다.
3. 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
4. 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 
비어있는 방 중 가장 번호가 작은 방을 배정합니다.

예를 들어, 방이 총 10개이고, 
고객들이 원하는 방 번호가 순서대로 [1, 3, 4, 1, 3, 1] 일 경우 다음과 같이 방을 배정받게 됩니다.
"""

####### 합계: 78.8 / 100.0 #######
####### 시간초과 #######
from collections import deque
import time

def solution(k, room_number):
    index = 0
    stack = deque()
    result = {i : True for i in range(1, k+1)}
    # print(result)
    for num in room_number :
        if num not in stack and result[num]:
            stack.append(num)
            result[num] = False
        else :
            # resultList = list(result.values())
            # print(resultList[num+1:])
            for i in range(num+1, num+1+k) :
                if result[i%k] == True :
                    stack.append(i%k)
                    result[i%k] = False
                    break
        if index == len(room_number) :
            break
    return list(stack)

start = time.time()
print(solution(10,[1,3,4,1,3,1]))
end = time.time()
print(f"{end - start:.5f} sec")


start = time.time()
print(solution(10**4,[1,3,4,1,3,1]))
end = time.time()
print(f"{end - start:.5f} sec")


print("{0:=^30}".format(" 구글링한 코드 "))

import sys
#recursionlimit을 지정해 주지않으면 런타임 에러가 뜨는 까다로운 프로그래머스...
sys.setrecursionlimit(10000000)

def solution(k, room_number):
    def dfs(n, rooms):
    	#비어있는 방이면 해당 방 번호의 다음 번호를 저장해놓는다
        if n not in rooms:
            rooms[n] = n + 1
            return n
        
        #현재 번호의 방이 비어있지않으면 해당 번호에 저장되어 있는 번호로 가본다.
        empty_room = dfs(rooms[n], rooms)
        #비어있는 방을 찾았다! 찾은 방은 현재 고객이 들어가야하니 다음 방을 저장해준다.
        rooms[n] = empty_room + 1
        return empty_room
    
    rooms = {} #현재 방 번호의 다음 번호 중 비어있는 방 번호를 저장
    answer = []
    for i in room_number:
        answer.append(dfs(i, rooms)) #배정된 방 번호 기록
        print(f"### 손님이 원하는 방 번호는 {i}입니다. ###")
        print(f"rooms : {rooms}\nanswer : {answer}\n")
            
    return answer

start = time.time()
print(solution(10,[1,3,4,1,3,1]))
end = time.time()
print(f"{end - start:.5f} sec")


start = time.time()
print(solution(10**4,[1,3,4,1,3,1]))
end = time.time()
print(f"{end - start:.5f} sec")

def solution(k, room_number):
    rooms = {}
    answer = []
    for n in room_number:
        visited = [n] #비어있는 방을 찾기 전 방문해본 방들
        #비어있는 방을 찾을 때까지 반복
        while n in rooms:
            n = rooms[n]
            visited.append(n)
        answer.append(n)
        #방문했던 방들에 현재 고객이 찾은 비어있는 방 번호의 다음 번호를 저장
        for i in visited:
            rooms[i] = n + 1
    return answer

start = time.time()
print(solution(10,[1,3,4,1,3,1]))
end = time.time()
print(f"{end - start:.5f} sec")


start = time.time()
print(solution(10**4,[1,3,4,1,3,1]))
end = time.time()
print(f"{end - start:.5f} sec")