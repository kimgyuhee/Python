a, b = map(int, input().split(" "))

s1 = set(input().split(" "))
s2 = set(input().split(" "))

print(len((s1-s2)|(s2-s1)))