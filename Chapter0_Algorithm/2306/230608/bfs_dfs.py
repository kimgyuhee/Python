"""
단지번호붙이기
https://www.acmicpc.net/problem/2667
"""

import sys
input = sys.stdin.readline
from collections import deque

# 값을 입력받아 기본 지도의 값을 채우기 위한 코드
# field = []
# for _ in range(int(input())) :
#     store = []
#     value = input()
#     for v in value :
#         if v.isdigit() :
#             store.append(int(v))

#     field.append(store)
# print(field)

import sys
input = sys.stdin.readline

n = int(input())
field = []

for _ in range(n):
    tmp = []
    for t in list(map(str, input().strip())):
        tmp.append(int(t))
    field.append(tmp)

def dfs(field, i, j) :
    value = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0] # 우, 좌, 하, 상
    stack = [[i, j]]
    while stack :
        x, y = stack.pop() 
        field[x][y] = -1
        for i in range(4) :
            a = x+dx[i]
            b = y+dy[i]

            if 0<=a<len(field) and 0<=b<len(field) and field[a][b] == 1 :
                value +=1
                field[a][b] = -1
                stack.append([a, b])

    return value
    

floor = 0
house_num = []
for i in range(len(field)) :
    for j in range(len(field)) :
        if field[i][j] <= 0 :
            field[i][j] = -1
        else :
            floor +=1
            value = dfs(field, i, j)
            house_num.append(value)

print(floor)
for num in house_num :
    print(num)

"""
다른 사람 풀이
"""
import sys
input = sys.stdin.readline

n = int(input())
lis = []

for _ in range(n):
    tmp = []
    for t in list(map(str, input().strip())):
        tmp.append(int(t))
    lis.append(tmp)

def dfs(lis, i, j):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    stack = [[i,j]]
    result.setdefault(count,[[i,j]])
    print("오잉?",result)

    while stack:
        a, b = stack.pop()
        lis[a][b] = -1
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and lis[x][y] == 1:
                result[count].append([x,y])
                lis[x][y] = -1
                stack.append([x,y])
                print(result)


count = 0
result = {}

for i in range(n):
    for j in range(n):
        if lis[i][j] == 0:
            lis[i][j] = -1
        if lis[i][j] == 1:
            count += 1
            dfs(lis, i, j)

print(len(result))
total = []
for key in result:
    total.append(len(result[key]))

total.sort()
for t in total:
    print(t)