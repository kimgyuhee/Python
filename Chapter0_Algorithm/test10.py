def solution(Directories, Cmd):
    answer = ''
    # nowl = Directories[0]
    s_D = Directories
    a = []
    indexA = 0
    nowl = Directories[indexA]
    for d in Directories :
        l = d.split("/")
        print(l)
        a.append(l)
    print(a)

    for c in Cmd :
        print("반복문 돌리는중")
        command, name = c
        # rmdir 명렁어 수행중
        if command == "rmdir" :
            removeOK = False
            index = 0
            removeIndex = 0
            for aa in a :
                if name in aa :
                    i = aa.index(name)
                    if i == len(aa)-1 :
                        removeIndex = index
                        print(removeIndex)
                        removeOK = True
                index +=1

            print(removeIndex)
            if removeOK :
                del a[removeIndex]

        # mkdir 명령어 수행중
        elif command == "mkdir" :
            mkOK = False
            index = 0
            for mm in a :
                if name not in mm :
                    mkOK = True

            if mkOK :
                Directories.append(nowl + "/" + name)
        # CD 명령어 수행중
        else :
            index = 0
            moveIndex = 0
            move = False 
            for mm in a :
                if name in mm :
                    moveIndex = index 
                    move = True
                index +=1

            if move :
                indexA = moveIndex

    answer = Directories[indexA]
    return answer



print(solution(["C:/root","C:/root/folder1","C:/root/folder2/file1.txt","C:/root/folder2/file2.txt"], [["rmdir","folder1"],["CD", "folder1"]]))