"""
사용자 입력과 출력
우리들이 사용하는 대부분의 완성된 프로그램은
사용자 입력에 따라 그에 맞는 출력을 내보낸다.
대표적인 예로 게시판에 글을 작성한 후 "확인" 버튼을 눌러야만(입력)
우리가 작성한 글이 게시판에 올라가는(출력) 것을 들 수 있다

"""

# 사용자 입력
import os


a = input()
print(a)

number = input("숫자를 입력하세요: ")

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short") # 1
print("life", "is","too short") # 2 문자열 띄어쓰기는 콤마로 한다
print("life"+"is"+"too short") # 3


"""
파일 읽고 쓰기
이번에는 파일을 통한 입출력 방법에 대해 알아보자.
여기에서는 파일을 새로 만든 다음 프로그램이 만든 결괏값을 새 파일에 적어볼 것이다.
또 파일에 적은 내용을 읽고, 새로운 내용을 추가하는 방법도 알아볼 것이다.
"""

# 파일 생성하기
# 파일 객체 = open(파일 이름, 파일 열기 모드)
f = open("새파일.txt", 'w')
f.close()

# /Users/gyuhee/Desktop/Python

"""
r   :   읽기모드 - 파일을 읽기만 할 때 사용
w	:   쓰기모드 - 파일에 내용을 쓸 때 사용
a	:   추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
"""

path = "/Users/gyuhee/Desktop/Python/File/"
file = path + "새파일.txt"
if os.path.isfile(file):
    print("이미 존재합니다.")
else :
    f = open(file, 'w')
    f.close()

    f = open(file, 'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()

# readline 함수 이용하기
f = open(file, 'r')
line = f.readline()
if('\n' in line):
    print("\\n 이 문단마다 들어갑니다.")
else :
    print("안들어가나봐요")
print(line)
f.close()

print("="*50)

f = open(file, 'r')
while True:
    line = f.readline()
    if not line: break
    print(line[:len(line)-1])
f.close()

print("="*50)
# readlines 함수 사용하기
f = open(file, 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line.strip())
f.close()

# read 함수 사용하기
f = open(file, 'r')
print(f)
data = f.read()
print(data)
f.close()

# 파일 객체를 for문과 함께 사용하기
f = open(file, 'r')
for line in f:
    print(line)
f.close()

# 파일에 새로운 내용 추가하기
# adddata.py
f = open(file,'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기
"""
파일을 열면(open) 항상 닫아(close) 주어야 한다.
하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까?
파이썬의 with문이 바로 이런 역할을 해준다.
다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.
"""
with open(path+"foo.txt", "w") as f:
    f.write("Life is too short, you need python")
