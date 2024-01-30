

N = int(input())
array = input().split(" ")
v = int(input())
result = 0
for a in array :
    if int(a)-v == 0:
        result +=1

print(result)