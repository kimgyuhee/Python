

import sys
from collections import deque

# 입력 받기
n = int(sys.stdin.readline())

balloons = deque([i for i in range(1, n+1)])
notes = deque(map(int, sys.stdin.readline().split()))

print(balloons)
print(notes)

result = []

order = balloons.popleft()
result.append(order)
move = notes[0]
while(len(balloons)!=0) :
    print("현재 풍선 순서 ", balloons, move)
    if move > 0 :
        for m in range(move) :
            balloons.append(balloons.popleft())
        order = balloons.pop()
        result.append(order)
        move = notes[order-1]
    else :
        for m in range(move*(-1)) :
            balloons.appendleft(balloons.pop())
        order = balloons.popleft()
        result.append(order)
        move = notes[order-1]

    print(order, move)
    print("\n반복문 돌았어여 ~")
    print(balloons)
    print("=========")

    print(result)

print(" ".join(map(str, result)))
