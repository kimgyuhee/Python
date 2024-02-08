
abc = list(map(int, input().split(" ")))

abc.sort()

print(abc)

if(abc[2]<abc[0]+abc[1]):
    print(sum(abc))
else :
    print(sum(abc)-((abc[2]-(abc[0]+abc[1]))+1))