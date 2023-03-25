"""
내장함수
# https://wikidocs.net/32
"""

# 1. abs : 절댓값을 리턴하는 함
print(abs(-4))
print(abs(48))
print(abs(-22.3))

# 2. all
"""
all(x)는 반복 가능한(iterable) 데이터 x를 입력 값으로 받으며
이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다

반복 가능한 데이터란 for 문에서 사용 가능한 자료형을 의미한다.
리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
"""
print(all([1, 2, 3])) #T
print(all(set("Hello"))) #T
print(all(set())) #T
print(all(set([1,2,3]))) #T
print(all([])) #T
print(all(set([1,2,3,0]))) #F
print(all([1, 2, 3, 0])) #F
print(all("")) #T
print(all(())) #T
print(all([])) #T
print(all({None})) #T -> F
print(all({""})) #T -> F


# 3. any
"""
any(x)는 반복 가능한(iterable) 데이터 x를 입력으로 받아 x의 요소 중 하나라도 참이 있으면 True를 리턴하고,
x가 모두 거짓일 때에만 False를 리턴한다. all(x)의 반대이다.
"""
print("{0:=^20}".format("any"))
print(any([1, 2, 3, 0])) #T
print(any([0, ""])) #F
print(any("")) #F
print(any(())) #F
print(any([])) #F

# 4. chr : chr(i)는 유니코드 숫자값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수
print("{0:=^20}".format("chr"))
print(chr(44032))
print(chr(97))
print(chr(65))
i = 65
while "python":
    if(chr(i) == 'z') :
        print(f"{chr(i)} -> {i}")
        break
    print(f"{chr(i)} -> {i}")
    i += 1


# 5. dir : 객체가 지닌 변수나 함수를 보여 주는 함수
print("{0:=^20}".format("dir"))
print(dir([1, 2, 3]))
print(dir({'1':'a'}))

# divmod
# divmod(a, b)는 2개의 숫자를 입력으로 받는다.
# 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴하는 함수
print("{0:=^20}".format("dir"))
print(divmod(7, 3))
t1 = divmod(8, 3)
print(t1)
print(type(t1))
print(t1[0])
print(t1[1])


# enumerate
# enumerate는 "열거하다"라는 뜻이다.
# 이 함수는 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
print("{0:=^20}".format("enumerate"))
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval
# eval(expression)은 문자열로 구성된 표현식을 입력으로 받아
# 해당 문자열을 실행한 결괏값을 리턴하는 함수
print("{0:=^20}".format("eval"))
print(eval('1+2'))
print(eval('divmod(4, 3)'))
print(eval("'hi' + 'a'"))

# filter
"""
filter 함수는 첫 번째 인수로 함수를,
두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
그리고 반복 가능한 데이터(iterable)의 요소 순서대로 함수(func)를 호출했을 때
반환 값이 참인 것만 묶어서(걸러 내서) 리턴
"""
print("{0:=^20}".format("ilter"))
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
print(filter(positive, [1, -3, 2, 0, -5, 6]))

# lambda를 사용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# hex
# hex(x)는 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수
print("{0:=^20}".format("hex"))
print(hex(234))
print(hex(3))

# oct
# oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수
print("{0:=^20}".format("oct"))
print(oct(234))
print(oct(3))
print(oct(12345))

# id
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 리턴하는 함수
print("{0:=^20}".format("id"))
a = 3
b = a
print(id(a))
print(id(3))
print(id(b))

# input
# input([prompt])은 사용자 입력을 받는 함수이다.
# 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트
print("{0:=^20}".format("input"))
b = input("Enter: ")
print(b)

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다.
# 만약 정수가 입력되면 그대로 리턴한다.
print("{0:=^20}".format("int"))
print(int('3'))
print(int(3.4))
print(int('11', 2)) # 2진수 -> 10진수
print(int('1A', 16)) # 16진수 -> 10진수
print(int('14', 8)) # 8진수 -> 10진수
# print(int("3.4")) - Error

# isinstance
# isinstance(object, class) 함수는 첫 번째 인수로 객체,
# 두 번째 인수로 클래스를 받는다.
# 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True,
# 거짓이면 False를 리턴
print("{0:=^20}".format("isinstance"))
class Person: pass
a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))

# len
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수
print("{0:=^20}".format("len"))
print(len("python"))
print(len((1, 'a')))
print(len(set([1,3,4])))

# list
# list(iterable)는 반복 가능한 데이터(iterable)를 입력받아 리스트로 만들어 리턴하는 함수
print("{0:=^20}".format("list"))
print(list("python"))
a = [1, 2, 3]
b = list(a)
c = a
print(c)
print(b)
print(id(a))
print(id(c))
print(id(b))
print(id(b)==id(c))


# map
# map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
# map 함수는 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수
print("{0:=^20}".format("map"))
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
    return 2*x
print(list(map(two_times, [1,2,3,4])))
print(map(two_times, [1,2,3,4]))
print(list(map(lambda x : x*5, [1,2,3,4])))

# max & min
# max(iterable) 함수는 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수
# min(iterable) 함수는 max 함수와 반대로, 인수로 반복 가능한 데이터를 입력받아 그 최솟값을 리턴하는 함수
print("{0:=^20}".format("max & min"))
print(max([1, 2, 3]))
print(max("python"))
print(min([1, 2, 3]))
print(min("python"))

# ord
# ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수
# ord 함수는 chr 함수와 반대이다.
print("{0:=^20}".format("ord"))
print(ord('a'))
print(ord('가'))

# range
print("{0:=^20}".format("range"))
print(list(range(5)))
print(range(5, 10))
r = range(1, 10, 2)
print(list(range(5, 10)))
print(type(r))
print(list(r))

# round
# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 리턴하는 함수
print("{0:=^20}".format("round"))
print(round(4.6))
print(round(4.2))
print(round(5.678, 2))

# sorted
# sorted(iterable) 함수는 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
print("{0:=^20}".format("sorted"))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted(set([1,6,3,2])))
print(sorted((3, 2, 1)))

# sum
# sum(iterable) 함수는 입력 데이터의 합을 리턴하는 함수
print("{0:=^20}".format("sum"))
print(sum([1,2,3]))
print(sum((4,5,6)))
print()

# tuple
# tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다. 만약 입력이 튜플인 경우에는 그대로 리턴한다.
print("{0:=^20}".format("tuple"))
print(tuple("abc"))
print( tuple([1, 2, 3]))

# zip
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수
print("{0:=^20}".format("zip"))
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip("abc", "def")))

