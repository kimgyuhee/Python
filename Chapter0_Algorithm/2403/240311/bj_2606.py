import sys

n = int(sys.stdin.readline())
dic = {i+1 : set() for i in range(n)}
route = [False for i in range(n)]
m = int(sys.stdin.readline())

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)


print(dic)
virus = set([1])
folder = set(dic[1])
start = 1
route[0] = True

for i in range(10) :
    print(route)
    print(dic)
    n = dic[start].pop()
    route[n-1] = True
    virus.add(n)
    folder.union(dic[n])
    start = n

print(dic)
print(virus)
