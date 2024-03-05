from collections import deque
import sys

N, K = map(int, (sys.stdin.readline().split(" ")))

circle = deque([i for i in range(1, N+1)])
result = []
remove_list = []
index = K-1
while(len(result)!=N):
    print(circle, result, index)
    if(index > len(circle)-1) :
        index = index%len(circle)
        print("index:", index, "=>", remove_list)
        for n in remove_list :
            circle.remove(n)
        remove_list = []
        if(index > len(circle)-1):
            index = index%len(circle)

    num = circle[index]
    result.append(num)
    index +=K    
    remove_list.append(num)
    print(result)

print(result)
"""

1, 3, 5, 7, 9, 
<3, 6, 2, 7, 5, 1, 4>
[2, (2+3)5, (2+3+3%7)8[1], (2+3+3+3%)11]
[2, 5, 1, 4, 2, 0, 0]


1, 2, 3, 4, 5, 6, 7
"""