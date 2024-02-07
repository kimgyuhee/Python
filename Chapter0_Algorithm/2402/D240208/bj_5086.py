
a = 1
b = 1
result = []
while(1) :
    a, b = list(map(int, input().split(" ")))
    if a==0 and b==0 :
        break
    elif b%a == 0 :
        result.append("factor")
    elif a%b == 0 :
        result.append("multiple")
    else :
        result.append("neither")

print("\n".join(result))

