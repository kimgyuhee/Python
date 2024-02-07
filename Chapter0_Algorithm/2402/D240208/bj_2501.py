
N, K = list(map(int, input().split(" ")))

lists = []

for i in range(1, (N+1)//2) :
    if(N%i==0) :
        if(i not in lists) :
            lists.append(i)
        if(N//i not in lists) :
            lists.append(N//i)

lists.sort()

if len(lists) < K :
    print(0)
else :
    print(lists[K-1])