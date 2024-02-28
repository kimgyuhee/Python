
from math import gcd

def gcd_N(arr) :
    g = arr[0]
    for a in arr :
        g = gcd(g, a)
    return g

n = int(input())

colonnade = []
first = int(input())

for i in range(1, n) :
    num = int(input())
    diff = num-first
    first = num
    colonnade.append(diff)

print(colonnade)
interval = gcd_N(colonnade)

print((sum(colonnade)-(len(colonnade)*interval))//interval)