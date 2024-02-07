
print(ord('A'))
print(chr(90))
print(chr(97))


B_N = input().split(" ")
B = B_N[0]
N = int(B_N[1])

result = 0

for i in range(len(B)) :
    mul = N ** i
    str = B[len(B)-i-1]
    if str.isdigit() :
        result += (mul * int(str))
    else :
        result += (mul * (ord(str)-55))

print(result)