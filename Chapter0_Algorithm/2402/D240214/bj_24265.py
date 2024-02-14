"""
1 (2 ~ 6) 5
2 (3 ~ 6) 4
3 (4 ~ 6) 3
4 (5 ~ 6) 2
5 (6 ~ 6) 1
-> 15 
"""

n = int(input())
sum = 0
for i in range(1, n):
    sum +=i

print(sum)
print(2)