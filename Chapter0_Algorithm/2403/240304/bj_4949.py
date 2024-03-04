import sys

o = ["[", "("]
c = ["]", ")"]
sets = ["[]", "()"]

stack = []
result = []

str = ""
while(str!="."):
    str = sys.stdin.readline().rstrip("\n")
    if str == ".":
        break
    check = "yes"
    for s in str :
        if s in o :
            stack.append(s)
        elif s in c :
            if len(stack) == 0 :
                check = "no"
                break
            p = stack.pop()
            if p+s not in sets :
                check = "no"
                break

    if len(stack)!=0 :
        check = "no"
        
    result.append(check)


for r in result :
    print(r)