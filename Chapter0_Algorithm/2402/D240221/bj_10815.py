import math
import time

start = time.time()

import sys
input = sys.stdin.readline
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
m_arr= list(map(int,input().split()))



for i in range(m):
    if m_arr[i] in arr : 
        print(1,end=' ')
    else : print(0,end=' ')

math.factorial(100000)
end = time.time()
print(f"{end - start:.5f} sec")