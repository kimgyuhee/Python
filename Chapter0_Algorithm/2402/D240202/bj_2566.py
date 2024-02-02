
result = 0
a, b = 0, 0
for i in range(9) :
    n = list(map(int, input().split(" ")))
    if result <= max(n) :
        result = max(n)
        a = i+1
        b = n.index(max(n))+1

print(result)
print(a, b)


l = [1, 2, 3, 4, 100]
print(max(l))
print(l.index(2))
print(l.index(100))