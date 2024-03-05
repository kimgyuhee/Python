from collections import deque
import sys

N = int(sys.stdin.readline())

card = deque([i for i in range(1, N+1)])

even = False
while(len(card)!=1) :
    num = card.popleft()
    if(even) :
        card.append(num)
    even = not even
    # print(card)
        

print(card[0])