
N, M = list(map(int, input().split(" ")))

s1 = set()

result = 0
for i in range(N):
    s1.add(input())

for i in range(M):
    str = input()
    if str in s1 :
        result +=1

print(result)