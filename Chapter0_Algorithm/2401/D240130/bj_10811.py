

a = [1, 2, 3, 4, 5, 6, 7]
print(a[1:2][::-1])
print(a)


N, M = input().split(" ")

assembly = [ i+1 for i in range(int(N))]

for i in range(int(M)):
    m = input().split(" ")
    a = int(m[0])-1
    b = int(m[1])
    
    assembly = assembly[:a] + assembly[a:b][::-1]+assembly[b:]
    
result = " ".join(map(str, assembly))

print(result)
