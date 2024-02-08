"""
              *
|
20                             *
|
|
10     *
|
|
------10------20------30------40


"""
# 시간초과 코드
# N = int(input())

# xlist = []
# ylist = []
# for i in range(N) :
#     x, y = list(map(int, input().split(" ")))
#     if x not in xlist :
#         xlist.append(x)
#     if y not in ylist :
#         ylist.append(y)

# X = max(xlist)-min(xlist)
# Y = max(ylist)-min(ylist)

# print(X*Y)


N = int(input())

x_max = -10000
x_min = 10000
y_max = -10000
y_min = 10000

for i in range(N) :
    x, y = list(map(int, input().split(" ")))
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x

    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y


X = x_max - x_min
Y = y_max - y_min

print(X*Y)
