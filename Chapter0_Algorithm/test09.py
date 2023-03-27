"""
파일 시스템을 관리하는 콘솔 프로그램을 개발한다. 파일 시스템은 윈도우와 동일한 폴더 구조를 가지고 있는데, 폴더와 파일로 구성된다.

C:/root/folder1 C:/root/folder2/file1.txt C:/root/folder2/file2.txt

위의 예시에서는 3개의 폴더가 존재하고 ("root", "root/folder1","root/folder2") "C:/root/folder2/" 경로에는 2개의 파일이 존재한다. ("file1.txt","file2.txt")

해당 프로그램은 입력된 디렉토리 정보를 입력 받고 실행되며, 현재 경로에서 폴더와 파일을 관리할 수 있는 다양한 명령어를 지원한다. 명령어의 형태는 다음과 같이, 명령어와 값으로 구성된다.

["명령어","값"]

명령어의 값이 경로를 표현하는 경우에는 절대 경로와 상대 경로를 모두 지원한다. 절대 경로 (["CD","c:/root"])인 경우에는 현재 사용자의 경로와 무관하게 동작하며, 상대 경로 (["CD","folder1"])인 경우에는 현재 사용자의 폴더 경로를 기준으로 동작한다.

지원되는 명령어와 동작의 설명은 다음과 같다.

명령어	동작
["CD","C:/root/folder1"]	"C:/root/folder1" 폴더로 이동
["mkdir","C:/root/folder2"]	"C:/root/folder2" 폴더를 생성한다
["rmdir","C:/root/folder1"]	"C:/root/folder1" 폴더를 삭제한다
"CD" 명령은 이동하려는 폴더가 없으면 이동하지 않고 현재 경로를 유지한다. "mkdir" 명령은 폴더를 생성할 경로가 존재하지 않거나, 이미 존재하는 경우에는 폴더가 만들어 지지 않는다. "rmdir" 명령은 삭제할 폴더가 존재하지 않거나, 폴더에 파일이나 폴더가 있다면 삭제할 수 없다. 또한, 삭제할 폴더가 사용자가 현재 경로에 포함된다면 삭제할 수 없다.

요청된 프로그램을 개발하시오.

입력
첫 번째 입력으로 폴더와 파일의 정보가 Directories1, ...,DirectoriesN이 문자열 배열로 주어진다. 파일의 경우에는 확장자가 포함되어 있고, 폴더의 경우에는 확장자가 없다. 입력된 배열의 첫 번째 값은 반드시 폴더의 경로이며, 상대 경로의 기준이 되는 현재 사용자의 폴더이다.

두 번째 입력은 명령어와 값의 쌍 Cmd1, ..., CmdN이 이중 배열로 주어진다. 명령어와 값의 쌍은 두 개의 문자열로 구성되며, 첫 번째 인자는 명령어, 두 번째 인자는 명령어 수행에 필요한 값이다.

출력
프로그램을 수행하고 사용자의 현재 경로를 문자열로 반환한다. (절대 경로로 반환한다.)

입출력 예제 1
Directories	Cmd	return
["C:/root","C:/root/folder1","C:/root/folder2/file1.txt","C:/root/folder2/file2.txt"]	[["rmdir","folder1"],["CD", "folder1"]]	"C:/ro
"""
def solution(Directories, Cmd):
    answer = ''
    nowl = Directories[0]
    a = []
    for d in Directories :
        l = d.split("/")
        print(l)
        a.append(l)
    print(a)

    for c in Cmd :
        print("반복문 돌리는중")
        command, name = c
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

        print(a)


    return answer



print(solution(["C:/root","C:/root/folder1","C:/root/folder2/file1.txt","C:/root/folder2/file2.txt"], [["rmdir","folder1"],["CD", "folder1"]]))