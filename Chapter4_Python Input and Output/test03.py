"""
프로그램의 입력과 출력
"""

# import sys
# args = sys.argv[1:]
# for i in args :
#     print(i)

import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

"""
터미널 사용하기
- 실행 : command + space를 누르고 '터미널' 이라고 입력하면 실행

1. 탐색하기
* ls : 현재 경로에 존재하는 파일/폴더 확인하기
* pwd : 현재 위치한 경로 출력하기
* cd : 디렉토리 이동하기

2. 파일/폴더 관리하기
* touch : 파일 생성하기
* mkdir : 폴더 생성하기
* cat : 파일 확인하기
* rm : 파일 삭제하기
    rm -r : 파일을 갖고 있는 폴더 삭제하기
* rmdir : 폴더 삭제하기
* cp : 파일/폴더 복사하기
* mv : 파일/폴더 이동시키기, 이름 변경하기

3. 기타 유용한 명령어
* clear : 터미널 정리하기
* history : 이전에 사용한 명령어 확인하기
* man : 명령어 매뉴얼 확인하기

"""