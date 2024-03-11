import sys

N, K = map(int, sys.stdin.readline().split())

cable = []

for _ in range(N) :
    cable.append(int(sys.stdin.readline()))

cable.sort()
count = 0
avg = sum(cable)//K

while(True) :
    print("=>", avg)
    for c in cable :
        num = c//avg
        print(c//avg)
        count +=num
    print("========> ",count)
    if(count >= K) :
        break
    avg -=1
    count = 0

print("result -> ", avg)

import sys

N, K = map(int, sys.stdin.readline().split())

cable = []

for _ in range(N) :
    cable.append(int(sys.stdin.readline()))

# cable.sort()
count = 0
avg = sum(cable)//K

while(True) :
    #print("=>", avg)
    for c in cable :
        num = c//avg
        #print(c//avg)
        count +=num
    #print("========> ",count)
    if(count >= K) :
        break
    avg -=1
    count = 0

#print("result -> ", avg)
print(avg)