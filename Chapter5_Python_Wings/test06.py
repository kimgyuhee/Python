"""
표준 라이브러리
"""

import os
# 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ
print(os.environ)
for i in range(10) :
    print()
# 디렉터리 위치 변경하기 - os.chdir
print(os.chdir("/Users/gyuhee/Desktop/Python/File"))
# 디렉터리 위치 돌려받기 - os.getcwd
print(os.getcwd())
# 시스템 명령어 호출하기 - os.system
print(os.system("ls"))
# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
f = os.popen("ls")
print(f.read())

# 기타 유용한 os 관련 함수
"""

os.mkdir(디렉터리) - 디렉터리를 생성한다.
os.rmdir(디렉터리) - 디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
os.unlink(파일) - 파일을 지운다.
"""

import zipfile

try : 
    with zipfile.ZipFile('mytext.zip', 'w') as myzip:
        myzip.write('a.txt')
        myzip.write('b.txt')
        myzip.write('c.txt')
except FileNotFoundError:
    f = open("a.txt", 'wb')
    f = open("b.txt", 'wb')
    f = open("c.txt", 'wb')
    f.close()


with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()
