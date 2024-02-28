

n = int(input())
check = [0] * (n+1)

for i in range(1, n+1) :
    for j in range(i, n+1, i) :
        if(check[j] == 0 ) :
            check[j] = 1
        else :
            check[j] = 0

print(sum(check))


cnt = 0
for i in range(1, n+1):
    if i**2 <= n:
        cnt += 1
    else:
        break

print(cnt)