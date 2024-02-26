# N, M = map(int, input().split(" "))

# print(N, M)

# print(N)

# encyclopedia1 = dict()
# encyclopedia2 = dict()

# for i in range(N):
#     pokemon = input()
#     num = i+1
#     encyclopedia1[str(num)] = pokemon
#     encyclopedia2[pokemon] = str(num)

# result = []

# for i in range(M) :
#     quiz = input()
#     if quiz.isdigit() :
#         result.append(encyclopedia1[quiz])
#     else :
#         result.append(encyclopedia2[quiz])

# # print("="*30)
# for r in result :
#     print(r)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])