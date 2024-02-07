
N = int(input())
n = 2
list = []
while(1):
    if(N ==1) :
        break
    elif(N==n) :
        list.append(n)
        print(n)
        break
    else :
        if(N%n==0):
            N = N//n
            list.append(n)
            print(n)
        else :
            n+=1

print(list)




