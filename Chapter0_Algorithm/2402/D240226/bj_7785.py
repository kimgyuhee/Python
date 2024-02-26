
import sys
n = int(input())

# s1 = set()
# s2 = set()

# for _ in range(n) :
#     name, commute = list(input().split(" "))
#     if commute == "enter" :
#         s1.add(name)
#     else :
#         s2.add(name)

# result = list(s1.difference(s2))
# result.sort()
# result.reverse()
# print("\n".join(result))


r = set()
for _ in range(n) :
    name, commute = list(input().split(" "))
    if commute == "enter" :
        r.add(name)
    else :
        r.remove(name)

print("\n".join(sorted(list(r), reverse=True)))
