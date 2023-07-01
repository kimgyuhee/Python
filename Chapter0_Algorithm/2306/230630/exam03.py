def dfs(grid, i, j, d, k):
    answer = True
    dk = d*k
    # print(dk)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0] # 우, 좌, 하, 상
    stack = [[i,j]]
    # print("stack의 값은 ?", stack)
    while stack:
        # print("뭐야")
        for di in dk :
            result = False
            print("a와 b의 값은 ? ")
            a, b = stack.pop()
            print(f"{a}, {b}, {grid[a][b]}")
            # grid[a][b] = -1
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) :
                    if grid[x][y]-grid[a][b] == di :
                        print(f"grid[x][y]-grid[a][b] : {grid[x][y]-grid[a][b]}")
                        result = True
                        # grid[x][y] == -1
                        stack.append([x,y])
                        break

            if result == False :
                answer = False
                break

        if result == False :
                break

    return answer

def solution(grid, d, k) :
    answer = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            print(i, j)
            grid = grid.copy()
            print(grid)
            if dfs(grid, i, j, d, k) :
                answer +=1
    print("정답은 ??????????")
    return answer


print(solution([[3,6,11,12],[4,8,15,10],[2,7,0,16]],[1,-2,5],3))
f=[3,2,1]
print(f*2)