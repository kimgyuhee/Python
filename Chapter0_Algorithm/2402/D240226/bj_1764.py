N, M = map(int, input().split(" "))

s1 = set()

for i in range(N):
    name = input()
    s1.add(name)

result = []
for i in range(M):
    name = input()
    if name in s1 :
        result.append(name)


print(len(result))
result.sort()
for r in result :
    print(r)
