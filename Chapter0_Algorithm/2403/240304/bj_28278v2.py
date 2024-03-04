import sys


n = int(sys.stdin.readline())

stack =[]
result = []

for i in range(n) :
    command = sys.stdin.readline().rstrip("\n")
    print(command)

    if len(command) != 1 :
        a = command.split(" ")[1]
        stack.append(int(a))
    elif command == "2":
        if len(stack) == 0 :
            print(-1)
        else :
            num = stack.pop()
            print(num)
    elif command == "3":
        print(len(stack))
    elif command == "4" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    else :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[len(stack)-1])

