N, M = input().split(" ")

array = [ i+1 for i in range(int(N))]

for i in range(int(M)):
    m = input().split(" ")
    a = int(m[0])-1
    b = int(m[1])-1
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

result = " ".join(map(str, array))

print(result)
