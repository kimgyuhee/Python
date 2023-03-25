"""
패키지
패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다
import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
"""

# __init__.py 의 용도
"""
python3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다.
하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.
"""

"""
에외처리
- 없는 파일을 열려고 시도하면 FileNotFoundError 오류가 발생
- 4를 0으로 나누려니까 ZeroDivisionError 오류
- a는 리스트 [1, 2, 3]이므로 a[4]는 a 리스트에서 얻을 수 없는 값이다
따라서 IndexError 오류
"""

# 오류 예외 처리 기법
# 1. try, except문
"""
try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.
"""

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


# 2. try .. finally
"""
try문에는 finally절을 사용할 수 있다.
finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행
"""
try:
    f = open('foo.txt', 'w')
    print("오류가 났는데 아래 문장도 계속 실행되는건가?")
    4 / 0
except IndexError:
    print("인덱싱 할 수 없습니다.")
except FileNotFoundError as e :
    print(e)
    print("파일을 열때 오류가 났어요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
finally :
    print("헤 오류는 안났지롱 파일 닫는다~")
    f.close()

# try ... else
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

# 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    pass

eagle = Eagle()
try :
    eagle.fly()
except Exception as e:
    print(e)
    print("에러 발생 raise 했지롱")
else : 
    print("에 너 출력되면 안되는데?")

# 예외 만들기
# class MyError(Exception):
#     print("하하핳ㅎ하하핳핳")
#     pass

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try :
    say_nick("천사")
    say_nick("바보")
    
except MyError as e:
    print("허용되지 않는 별명입니다.")
    print(e)