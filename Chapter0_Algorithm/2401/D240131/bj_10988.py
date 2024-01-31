
str = input()

n = len(str)//2

first = str[:n]

if len(str)%2 == 0 :
    seconde = str[n:][::-1]
else :
    seconde = str[n+1:][::-1]


print(first, seconde)

if first == seconde :
    print(1)
else :
    print(0)
# 1 2 3 4 5 6 7 8 9