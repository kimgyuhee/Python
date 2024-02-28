# 시간초과
import math

def is_prime_number(x) :
    result = False
    for i in range(2, int(math.sqrt(x))+1) :
        if(x%i == 0) :
            result = True
            break
    if x == 1 :
        return True
    return result

n = int(input()) 
result = []

for i in range(n):
    num = int(input())
    s = set()
    for j in range(2, num) :
        if(not is_prime_number(j)):
            if(not is_prime_number(num-j)) :
                if(j not in s) :
                    s.add(num-j)

    result.append(len(s))

for r in result :
    print(r)