
n = int(input())

str_empty = " "
str_star = "*"
for i in range(2*n-1):
    e = abs((n-i)-1)
    if i < n :
        s = i*2+1
    else :
        s = abs(i-(2*n-2))*2+1
    print(str_empty*e + str_star*s)