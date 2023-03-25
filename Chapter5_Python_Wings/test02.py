"""
모듈
- 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

"""

# 모듈 만들기
# mod1.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b
"""
위와 같이 add와 sub 함수만 있는 파일 mod1.py를 만들고
디렉터리에 저장하자. 이 mod1.py 파일이 바로 모듈이다.

- 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다.
"""

import test01
from test01 import MoreFourCal

# 모듈 불러오기
# import 모듈이름
if __name__ == "__main__" : 
    print(test01.Family.lastname)
    test01.MoreFourCal(5, 2).print()
    MoreFourCal(4, 2).print()

"""
if __name__ == "__main__"을 사용하면
C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는
__name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다.
반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는
__name__ == "__main__"이 거짓이 되어
if문 다음 문장이 수행되지 않는다.
"""

# __name__ 변수란?
"""
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우
mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는
mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
"""

# 클래스나 변수 등을 포함한 모듈
# mod2.py 
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 

# >>> print(mod2.add(mod2.PI, 4.4))
# 7.541592

# 다른 파일에서 모듈 불러오기
# 모듈을 불러오는 또 다른 방법
"""
해당 모듈이 있는 디렉터리로 이동한 후에야 그 모듈을 사용할 수 있었다.
이번에는 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법
"""
###### 터미널에서 #######
# 1. sys.path.append 사용하기
# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.

# 2. PYTHONPATH 환경 변수 사용하기
# set PYTHONPATH=C:\doit\mymod
# 맥이나 유닉스 환경에서는 set 대신 export 명령을 사용해야 한다.