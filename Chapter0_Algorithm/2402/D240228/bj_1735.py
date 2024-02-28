
from math import gcd


A1, B1 = map(int, input().split(" "))
A2, B2 = map(int, input().split(" "))

# G1 = gcd(A1, B1)
# G2 = gcd(A2, B2)

# A1, B1 = A1//G1, B1//G1
# A2, B2 = A2//G2, B2//G2

# A = A1*B2 + A2*B1
# B = B1*B2

# print(A, B)

A = A1*B2 + A2*B1
B = B1*B2
G = gcd(A, B)

print(A//G, B//G)

