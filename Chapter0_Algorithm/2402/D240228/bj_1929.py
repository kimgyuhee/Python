
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

n, m = map(int, input().split(" "))

for i in range(n, m+1) :
    if(not is_prime_number(i)):
        print(i)