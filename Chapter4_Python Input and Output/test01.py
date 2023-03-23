"""
함수
Q. 함수란 무엇인가?
    A. 함수를 설명하기 전에 믹서를 생각해 보자.
    우리는 믹서에 과일을 넣는다.
    그리고 믹서를 사용해서 과일을 갈아 과일 주스를 만든다.
    우리가 믹서에 넣는 과일은 "입력"이 되고
    과일 주스는 "출력(결괏값)"이 된다.
    (믹서는 과일을 입력받아 주스를 출력하는 함수와 같다.)

Q. 함수를 사용하는 이유는 무엇일까?
    A. "반복적으로 사용되는 가치 있는 부분"을 한 뭉치로 묶어서
    "어떤 입력값을 주었을 때 어떤 결괏값을 돌려준다"라는
    식의 함수로 작성하는 것이 현명

"""

# 매개변수와 인수
def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수
"""
# 매개변수 - 함수에 전달된 값을 저장하는 변수
# 인수 - 함수에 전달하는 값
"""
# 입력값이 없는 함수
def say(): 
    return "Hi"
a = say()
print(a)

# 리턴값이 없는 함수
def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

a = add(3, 7)
print(a) # None : 거짓을 나타내는 자료형, 리턴값이 없다는 것을 의미

# 입력값도 리턴값도 없는 함수
def say(): 
    print('Hi')
say()

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args): 
    result = 0
    for i in args: 
        result = result + i 
    return result

result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args): 
    if choice == "add": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result 

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 매개변수 kwargs -> **
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
"""
 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고
 모든 key=value 형태의 입력값이 그 딕셔너리에 저장된다는 것을 
 알수 있다.
"""

# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b): 
    return a+b, a*b

result = add_and_mul(3,4)
print(result)
print(type(result))

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)
print(result1 + result2)

def add_and_mul(a,b): 
    return a+b
    return a*b

result = add_and_mul(2, 3)
print(result)

# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다

## 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

say_myself("박응선", 27, False)

"""
초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓아야 함을 잊지 말자.
안그러면 아래와 같은 에러가 발생한다.
SyntaxError: non-default argument follows default argument
"""

# 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓아야 함을 잊지 말자.
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# return 사용하기
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1 
def vartest(): 
    global a # 전역변수 a
    a = a+1

vartest() 
print(a)

def globalDef():
    # global a 함수 사용안됨
    a = 10
    print("hi"*a)

globalDef()
print(a)
"""
프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다.
왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다. 
외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다
"""

# lambda
"""
lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할
보통 함수를 한줄로 간결하게 만들 때 사용한다. 
함수명 = lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
"""
add = lambda a, b : a+b
result = add(3, 4)
print(result)
