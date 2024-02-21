

n = int(input())
coordinate = list(map(int, input().split(" ")))
arr = sorted(list(set(coordinate)))
print(arr)
dic = {arr[i] : i for i in range(len(arr))}

print(dic)

for i in coordinate:
    print(dic[i], end = ' ')

