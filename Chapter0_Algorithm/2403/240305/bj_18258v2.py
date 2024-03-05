import sys

N = int(sys.stdin.readline())

queue = []
result = []

for i in range(N) :
    command = sys.stdin.readline().rstrip("\n")
    if(command[:4]=="push") :
        queue.append(int(command[5:]))
    elif(command == "pop") :
        if(len(queue) == 0) :
            result.append(-1)
        else :
            queue = queue[::-1]
            num = queue.pop()
            result.append(num)
            queue = queue[::-1]
    elif(command == "size") :
        result.append(len(queue))
    elif(command== "empty") :
        if(len(queue)==0):
            result.append(1)
        else:
            result.append(0)
    elif(command == "front") :
        if(len(queue)==0) :
            result.append(-1)
        else :
            result.append(queue[0])
    elif(command=="back") :
        if(len(queue)==0) :
            result.append(-1)
        else :
            result.append(queue[len(queue)-1])



print("~~~~~~~~~~~~ 출력결과 ~~~~~~~~~~~~")
for r in result :
    print(r)