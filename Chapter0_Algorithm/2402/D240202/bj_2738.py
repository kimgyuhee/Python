n = input().split(" ")
N = int(n[0])
M = int(n[1])

arrays = [[0 for i in range(M)] for j in range(N)]

for i in range(2) :
    for j in range(N):
        m = list(map(int, input().split(" ")))
        for k in range(M):
            arrays[j][k]+=m[k]


for i in range(N):
    print(" ".join(map(str,arrays[i])))