a, b, c, d, e, f = list(map(int, input().split(" ")))

check = False
print(a, b, c, d, e, f)
y = 0

for i in range(-999, 1000) :
    # print(d*((c//a)-(b//a)*i) + e*i )
    if d*(c//a)-d*(b//a)*i + e*i == f :
    # if (a-d)*((c//a)-((b//a)*y)) +(b-e)*y == c-f :
        y = i
        break

x = (c//a)-(b//a)*y
print(x, y)

for i in range(-999,1000):
    if(check):
        break
    for j in range(-999,1000):
        if a*i + b*j == c and d*i + e*j == f:
            check = True
            print(i,j)
            break
