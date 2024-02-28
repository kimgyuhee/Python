from math import gcd


A, B = map(int, input().split(" "))

s1 = {1}
s2 = {1}

for i in range(2, A+1):
    if(A%i == 0) :
        s1.add(i)

for i in range(2, B+1):
    if(B%i == 0) :
        s2.add(i)



s3 = s1.intersection(s2)
print(A*B//max(s3))

A, B = map(int, input().split())

print(gcd(A, B))
print(A*B//gcd(A,B))
res = A*B

# 최대공약수 (유클리드 호제법)
while B:
    if A > B:
        A, B = B, A
    B %= A

# 최소공배수
print(res//A)

