"""
유기농 배추
https://www.acmicpc.net/problem/1012
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    print("반복문 가능?") # 가능
    M, N, K = map(int, input().split(" "))

    # 배추밭의 넓이
    filed = [[0]*M for i in range(N)]

    for f in filed :
        print(f)

    # 배추가 심어져 있는 위치를 입력받기 위한 반복문
    for _ in range(K) :
        y, x = map(int, input().split(" "))
        filed[x][y] = 1


    for f in filed :
        print(f)

    def dfs(field, i, j) :

        # 현 위치 상하좌우 주변 좌표
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0] 
        stack = [[i, j]]
        field[i][j] = -1

        while stack :
            a, b = stack.pop()

            for d in range(4) :
                x = a + dx[d]
                y = b + dy[d]
                if 0<=x<N and 0<=y<M and field[x][y] == 1:
                    field[x][y] = -1
                    stack.append([x, y])

    count = 0
    for i in range(N) :
        for j in range(M) :
            # print(filed[i][j], i, j)
            if filed[i][j] <= 0 :
                filed[i][j] = -1
            else :
                count +=1
                dfs(filed, i, j)
    
    print(count)







import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    M, N, K = map(int, input().split(" "))

    # 배추밭의 넓이
    filed = [[0]*M for i in range(N)]

    # 배추가 심어져 있는 위치를 입력받기 위한 반복문
    for _ in range(K) :
        y, x = map(int, input().split(" "))
        filed[x][y] = 1

    def dfs(field, i, j) :

        # 현 위치 상하좌우 주변 좌표
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0] 
        stack = [[i, j]]
        field[i][j] = -1

        while stack :
            a, b = stack.pop()

            for d in range(4) :
                x = a + dx[d]
                y = b + dy[d]
                if 0<=x<N and 0<=y<M and field[x][y] == 1:
                    field[x][y] = -1
                    stack.append([x, y])

    count = 0
    for i in range(N) :
        for j in range(M) :
            if filed[i][j] <= 0 :
                filed[i][j] = -1
            else :
                count +=1
                dfs(filed, i, j)
    
    print(count)





# 2등코드
import sys

num = int(sys.stdin.readline())

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

def bfs(x, y) :
    
    queue = [(x, y)]
    matrix[x][y] = 0 
    
    while queue :
        x, y = queue.pop(0)
        
        for i in range(4) :
            nx = x + row[i]
            ny = y + col[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
                
            if matrix[nx][ny] == 1 :
                queue.append((nx,ny))
                matrix[nx][ny] = 0

for i in range(num) :
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    matrix = [[0] * m for i in range(n)]
    count = 0
    
    for i in range(k) :
        
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
        
        
    for j in range(n) :
        for k in range(m) :
            if matrix[j][k] == 1:
                bfs(j, k)
                count += 1
    
    print(count)