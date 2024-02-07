
result = []

while(1):
    N = int(input())
    if N==-1:
        break

    lists = []
    for i in range(1, (N+1)//2) :
        if(N%i==0) :
            if(i not in lists) :
                lists.append(i)
            if(N//i not in lists) :
                lists.append(N//i)
    lists.sort()
    lists.remove(N)

    if sum(lists) != N :
        ex = f"{N} is NOT perfect."
    else :

        plus_ex = " + ".join(map(str, lists))
        ex = f"{N} = {plus_ex}"

    result.append(ex)


print("\n".join(result))


a = """
6 = 1 + 2 + 3
12 is NOT perfect.
28 = 1 + 2 + 4 + 7 + 14
"""

b = """
6 = 1 + 2 + 3
12 is NOT perfect.
28 = 1 + 2 + 4 + 7 + 14
"""

print(a==b)