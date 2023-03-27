def solution(n, m, x, y, z):
    answer = []
    return answer


def checkIntInput(a, b) :
    while 1:
        try :
            n = int(input(">>>"))
        except ValueError :
            print("숫자를 입력해주세요 :)"); continue
        else :
            if not(n >=a and n<=b) :
                print(f"{a}~{b} 사이의 숫자를 입력해주세요.")
                continue
            else :
                break
    return n

n = checkIntInput(2,400)
m = checkIntInput(n-1, n*(n-1)/2)

arrayIndex = 0
x = []
while True :
    if arrayIndex == n:
        break
    value = checkIntInput(1, n)
    x.append(value)
    arrayIndex +=1

print(x)
arrayIndex = 0
y = []
while True :
    if arrayIndex == n:
            break
    value = checkIntInput(1, n)
    if x[arrayIndex] == value:
        print("xi == yi")
        continue
    else :
        y.append(value)
        arrayIndex +=1

print(y)

z = []
for i in range(n) :
    value = checkIntInput(1, 100000)
    z.append(value)

print(z)

result = {}
for i in range(n):
    result[i+1] = 0

print(result)

for i in range(0, n):
    result[x[i]] = result.get(x[i]) + z[i]
    result[y[i]] = result.get(y[i]) + z[i]
    print(f"{x[i]}-{y[i]} => {z[i]}")

def minIndex(z) :
    return z.index(min(z))

def minValue(a, b):
    if a > b :
        return b, a
    else :
        return a, b

print(result)

answer = []

while len(answer) !=n :
    index = minIndex(z)
    print(index)
    z[index] = 100000
    a = x[index]
    b = y[index]
    first, second = minValue(a, b)
    if first not in answer :
        answer.append(first)
    if second not in answer :
        answer.append(second)

def checkKey(dict) :
    result = True
    value = dict.get(len(dict))
    print(value)
    d = dict.values()
    print(d)
    for i in d :
        if i != value :
            return False
    return result

a = checkKey(result)
print(a)
if checkKey(result) :
    answer = list(i for i in range(1, n+1)) 

print(answer)
"""
n	m	x	y	z	return
3	3	[1, 1, 2]	[3, 2, 3]	[1, 5, 2]	[1, 3, 2]

n	m	x	y	z	return
4	4	[1, 1, 3, 4]	[3, 4, 2, 2]	[2, 1, 1, 2]	[1, 2, 3, 4]
"""
