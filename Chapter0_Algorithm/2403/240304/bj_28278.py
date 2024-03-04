import sys


n = int(sys.stdin.readline())

stack =[]
result = []

for i in range(n) :
    command = sys.stdin.readline().rstrip("\n")

    if len(command) != 1 :
        a = command.split(" ")[1]
        stack.append(int(a))
    elif command == "2":
        if len(stack) == 0 :
            result.append(-1)
        else :
            num = stack.pop()
            result.append(num)
    elif command == "3":
        result.append(len(stack))
    elif command == "4" :
        if len(stack) == 0 :
            result.append(1)
        else :
            result.append(0)
    elif command == "5":
        if len(stack) == 0 :
            result.append(-1)
        else :
            num = stack[len(stack)-1]
            result.append(num)

for i in result :
    print(i)