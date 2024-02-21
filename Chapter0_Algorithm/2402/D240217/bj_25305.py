"""


"""

N, k = list(map(int, input().split(" ")))

l = list(map(int, input().split(" ")))
l.sort()
scores = l[::-1]

print(scores[k-1])