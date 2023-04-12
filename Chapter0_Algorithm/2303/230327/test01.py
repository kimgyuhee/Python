"""
멋진 풀이 
"""
dot = [2, -1]

quad = [(3,2), (4,1)]

print(quad[dot[0] > 0][dot[1] > 0]) # TF -> 4


dot = [-2, -1]
quad = [(3,2), (4,1)]

print(quad[dot[0] > 0][dot[1] > 0]) # FF -> 3

###################
l = [1,2,3,4,5]

print(min(l))
a = l.pop(min(l))
print(a)
print(l)

l.sort()
print(l)
print(l[-2]*l[-1])



a = [2,3,4,4,44,4,4,4]
print(a.count(4))
print(a.count(1000))


park = ["SOOOXOOO", "OXO", "OOO"]
print(park[0][min(1, 1) : max(2, 2)+1])
print(park[0][min(0, 1) : max(2, 2)+1])
print(park[0][min(0, 5) : max(0, 5)+1])

for row in park[min(0,0):max(2,2)] :
    print(row[1])

# print(a)