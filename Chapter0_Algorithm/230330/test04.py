"""
스택 & 큐
"""
from collections import deque
stack = []

stack.append(5)
stack.append(2)
stack.pop()
stack.append(1)
stack.append(9)

# 최상단 원소부터 출력
print(stack)
# 최하단 원소부터 출력
print(stack[::-1])

queue = deque()
print(queue)
queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
print(queue)
queue.append(9)
print(queue)

# 먼저 들어온 순서대로 출력
print(queue)
# 역순으로 바꾸기
queue.reverse()
# 나중에 들어온 원소부터 출력
print(list(queue))
