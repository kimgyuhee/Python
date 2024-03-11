cnt=0
def DFS(virus):
    print('virus, ', virus)
    print(visited)
    global cnt
    visited[virus]=1

    for i in network[virus]:
        if (visited[i]==0):
            print("network, i",i)
            DFS(i)
            cnt+=1


N= int(input())
link = int(input())

network = [[]*(N+1) for _ in range(N+1)]

print("\n반복문 들어가여 ~")
for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
    print(network)
print("\n양방향 네트워크 연결 성공\n")

visited = [0]*(N+1)
DFS(1)
print(cnt)