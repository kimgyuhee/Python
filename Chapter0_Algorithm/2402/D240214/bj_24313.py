a1, a0 = list(map(int, input().split(" ")))
c = int(input())
n0 = int(input())

fn = a1*n0+a0
gn = c*n0

if (fn <= gn and a1 <= c):
    print(1)
else :
    print(0)