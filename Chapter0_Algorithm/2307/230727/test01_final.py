def solution(m, n, b):
    b = [[[0, b[y][x], 0] for y in range(m)] for x in range(n)]
    ispoped = True
    while ispoped:
        ispoped = False
        for y in range(n-1):
            for x in range(m-1):
                if sum([b[y][x][0], b[y][x+1][0], b[y+1][x][0], b[y+1][x+1][0]]) == 0:
                    if len(set([b[y][x][1], b[y][x+1][1], b[y+1][x][1], b[y+1][x+1][1]])) == 1:
                        ispoped = True
                        b[y][x][2], b[y][x+1][2], b[y+1][x][2], b[y+1][x+1][2] = 1, 1, 1, 1

        for y in range(n-1):
            for x in range(m-1):
                b[y][x][0], b[y][x+1][0], b[y+1][x][0], b[y+1][x+1][0] = b[y][x][2], b[y][x+1][2], b[y+1][x][2], b[y+1][x+1][2]

        for i in range(len(b)):
            b[i].sort(key=lambda x: -x[0])

    answer = 0
    for y in range(n):
            for x in range(m):
                answer += 1 if b[y][x][0] == 1 else 0
    return answer