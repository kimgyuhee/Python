# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.

n = int(input())

l = []

for i in range(n) :
    age, name = input().split(" ")
    l.append([int(age), i, name])

l.sort()

for i in range(n) :
    print(l[i][0], l[i][2])

"""
A=int(input())
user = []
for _ in range(A):
    age, name = input().split()
    user.append([int(age),name])

for i in sorted(user,key=lambda x : x[0]):
    print(i[0],i[1])

"""