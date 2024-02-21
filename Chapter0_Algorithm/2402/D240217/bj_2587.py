
l = []
for i in range(5):
    n = int(input())
    l.append(n)

l.sort()
print(sum(l)//5)
print(l[2])