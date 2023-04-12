def solution(n, m, a, b, c, d):

    def minT(weight):
        min = 100
        for i in weight :
            if i < min :
                min = i
        return i
    
    weight1 = []
    for i in range(0, m) :
        weight1.append(c[i]*1+d[i])
    print(weight1)

    weight2 = []
    for i in range(0, m) :
        weight2.append(c[i]*2+d[i])
    print(weight2)


    result1 = minT(weight1)
    result2 = minT(weight2)

    print(f"result1 => {result1}")
    print(f"result2 => {result2}")

    if result1 != result2:
        if result1*result2 < 0 :
            answer = "INF"
        else :
            answer = result1
    else :
        if result1 == 0 :
            answer = "NONE"
        elif result1 < 0 :
            answer = "-INF"
        else :
            answer = result1

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

n = checkIntInput(1, 20000)
m = checkIntInput(1, 50000)
a = []
for i in range(0, m) :
    valueA = checkIntInput(1, n)
    a.append(valueA)
print(a)
b = []
for i in range(0, m) :
    while 1:
        valueB = checkIntInput(1, n)
        if(a[i] == valueB) :
            continue
        else :
            break
    b.append(valueB)
print(b)
c = []
for i in range(0, m) :
    valueC = checkIntInput(-1000, 1000)
    c.append(valueC)
print(c)
d = []
for i in range(0, m) :
    valueD = checkIntInput(-1000000, 1000000)
    d.append(valueD)
print(d)


result = solution(n, m, a, b, c, d)
print(result)