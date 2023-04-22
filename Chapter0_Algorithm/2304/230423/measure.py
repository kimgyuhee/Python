# 효율적인 약수 구하기

def measure(n) :
    numberSet = []
    for i in range(1, int(n**(1/2))+1) :
        if (n%i == 0) :
            numberSet.append(n//i)
            numberSet.append(i)
        
    answer = list(set(numberSet))
    return sorted(answer)

def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

print(measure(10))
print(measure(100))
print(measure(421))