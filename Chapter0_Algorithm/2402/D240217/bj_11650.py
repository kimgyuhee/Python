"""


"""

n = int(input())
points = []

for i in range(n):
    p = list(map(int, input().split(" ")))
    points.append(p)

points.sort()

print(points)

for i in range(n):
    print(points[i][0], points[i][1] )