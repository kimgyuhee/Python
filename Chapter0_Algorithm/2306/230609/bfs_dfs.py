
# 재귀로 풀 경우 재귀 깊이를 지정해주어야 한다.
import sys
sys.setrecursionlimit(100000)


"""
파이썬의 리스트는 스택처럼 동작하므로 dfs 구현시 그냥 리스트를 사용하면 된다.
bfs구현시 덱(deque)를 사용한다. (리스트로 .pop(0) 해도되지만 덱이 훨 빠르다.)
"""
from collections import deque
q = deque()
print(q) # []
qq = deque([1])
print(qq) # [1]


"""
방문했던 노드를 기록할 때 리스트보다 딕셔너리로 구현해야 빠르다. 
또는 인덱스를 이용해 0,1을 넣어주거나 하면 된다.
"""

# 예를 들어,
visit = [1,2,3]
if 4 in visit:
	pass
# 위와 같은 코드는, visit의 모든 노드를 살펴보아야함 O(N)

# 노드의 수가 5라고 하면
visit = [0]*5
if visit[4] == 1:
	pass
# 이런 식으로 인덱스를 지정하여 방문 노드를 검사하거나 딕셔너리를 이용한다.
# 기본적이지만 막 풀다보면 리스트를 남용해버리는 경우가 많다.


# 유기농 배추
# https://www.acmicpc.net/problem/1012
"""
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
"""
"""
def solution(M, N, K) :
	field = [[0] * M for _ in range(N)]
	
"""
import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    m, n, k = map(int, input().split())

    lis = [[0]*m for i in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        lis[y][x] = 1
    count = 0

    def dfs(lis, i, j):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0] # 우, 좌, 하, 상
        stack = [[i,j]]
        print("stack의 값은 ?", stack)
        while stack:
            print("a와 b의 값은 ? ")
            a, b = stack.pop()
            print(a, b)
            lis[a][b] = -1
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < n and 0 <= y < m and lis[x][y] == 1:
                    lis[x][y] == -1
                    stack.append([x,y])
                    print("stack에 왜 추가하지?", stack)

    
    for i in range(n):
        for j in range(m):
            print(n, m)
            if lis[i][j] <= 0:
                lis[i][j] = -1
            else:
                count += 1
                print("배추흰지렁이 추가합니다 ~ ")
                dfs(lis, i, j)

    print(count)