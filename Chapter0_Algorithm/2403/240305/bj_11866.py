from collections import deque
import sys

N, K = map(int, (sys.stdin.readline().split(" ")))

circle = deque([i for i in range(1, N+1)])
result = []
remove_list = []
index = K-1
while(len(result)!=N):
    num = circle[index%len(circle)]
    print(num, index, index%N)
    result.append(num)
    index +=K
    remove_list.append(num)
    # circle.remove(num)
    if(index >= len(circle)) :
        for n in remove_list :
            circle.remove(n)
        remove_list = []
        if index == 0 :
            index = (index+K-1)%N
        else :
            index = index%N
        print("index : ", index)
    print(circle)
    print(result)


"""
2+3+3
1, 2, 3, 4, 5, 6 , 7
3, 6, 2
"""