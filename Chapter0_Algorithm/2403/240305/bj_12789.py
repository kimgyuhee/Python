import sys

N = int(sys.stdin.readline())

line= list(map(int,sys.stdin.readline().split(" ")))[::-1]

stack1 = []
stack2 = []

now_order = 1

print(line)

while(len(stack1) != N) :
    if(now_order in stack2) :
        num2 = stack2.pop()
        if(now_order == num2) :
            now_order +=1
            stack1.append(num2)
            # for j in range(1, len(stack2)) :
            #     stack2[j-1] = stack2[j]
        else :
            break
    else :
        if(len(line)!=0) :
            num = line.pop()
            if(num==now_order) :
                now_order +=1
                stack1.append(num)
            else :
                stack2.append(num)
        else :
            print("뭔가 오류가 발생,")
            break
    
    print("stack1 => ",stack1)
    print("stack2 => ",stack2)
    print("now_order => ", now_order)

print(line)

if len(stack1) == N :
    print("Nice")
else :
    print("Sad")