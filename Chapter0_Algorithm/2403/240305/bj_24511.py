import sys
from collections import deque

# 입력 받기
n = int(sys.stdin.readline())
sequenceA = sys.stdin.readline().split()
sequenceB = sys.stdin.readline().split()
m = int(sys.stdin.readline())
sequenceC = sys.stdin.readline().split()

print(n)
print(sequenceA)
print(sequenceB)
print(sequenceC)
print(m)

result = []
for i in range(m):
    return_value = sequenceC[i]
    num = sequenceC[i]
    for j in sequenceA :
        if(j==0) :
            for k in range(n) :
                return_value = sequenceB[k]
                sequenceB[k] = return_value

    print(sequenceB)
    result.append(return_value)

print(result)

"""
import sys
from collections import deque

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))  # 0 1 1 0 (0 = queue, 1 = stack)
list_b = list(map(int, sys.stdin.readline().split()))  # 1 2 3 4

m = int(sys.stdin.readline())
list_c = list(map(int, sys.stdin.readline().split()))

res = deque()

for qs in range(n):
    if list_a[qs] == 0:
        res.appendleft(list_b[qs])
        
for i in range(m):
    res.append(list_c[i])
    print(res.popleft(), end=' ')


"""