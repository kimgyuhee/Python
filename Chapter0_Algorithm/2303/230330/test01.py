# 그리디 알고리즘

def solution(n, array) :
    count = 0
    for coin in array :
        count = count + (n//coin)
        print(f"coin : {coin}, count : {count}")
        n = n%coin

    return count


print(solution(1260, [500,100,50,10]))
print(solution(800, [500,400,100]))

def restOne(n, k) :
    result = 0
    while True :
        target = (n//k) * k
        print(f" target : {target} k : {k}")
        result += (n - target)
        n = target
        if(n < k ):
            break
        result +=1
        n = n //k

    result = result + (n-1)
    print(result)

restOne(25,3)


def solution(triangle):
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])


    return max(triangle[-1])

print(solution([[7]]))
print(solution([[7], [0,10]]))
