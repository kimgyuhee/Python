
n = int(input())
points = []

for i in range(n):
    p = list(map(int, input().split(" ")))

    points.append(p[::-1])

points.sort()

print(points)

for i in range(n):
    print(points[i][1], points[i][0])