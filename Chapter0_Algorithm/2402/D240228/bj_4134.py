
import math


def is_prime_number(x) :
    result = False
    for i in range(2, int(math.sqrt(x))+1) :
        if(x%i == 0) :
            result = True
            break
    return result

n = int(input())

result = []
for i in range(n) :
    num = int(input())
    if num == 1 or num == 0 :
        result.append(2)
        continue
    decimal = num
    while(is_prime_number(decimal)):
        decimal+=1

    result.append(decimal)

print("\n".join(map(str, result)))