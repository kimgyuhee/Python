"""
if 문
if 조건문에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다.
* 비교연산자(<, >, ==, !=, >=, <=)
* 조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다.
"""

"""
파이썬 연산자 종류
- 산술 연산자 (+, -, *, /, %, **, //)
- 할당 연산자 (=, +=, -=, *=, /=, %=, //=, **=)
- 삼항 연산자 (ex. (num % 2 === 0) ? a = 0 : a = 1)
- 비교 연산자 (<, >, ==, !=, >=, <=)
- 논리 연산자 (and, or, not)
- 항등 연산자 (==, is, is not)
- 멤버 연산자
- 비트 연산자 (&, |, ^, ~, <<, >>)
"""

# 멤버 연산자
a = 10
b = [1, 10, 3, 4, 65, 8]
c = 9

if a in b:
    print('a가 b 리스트 안에 있습니다.')
    
if not c in b: 
    print('c가 b 리스트 안에 없습니다.')


# 비트 연산자
a = 0b10101010
b = 0b01110011
c = 0b11011001
print('a = ', a, ":", bin(a))
print('b = ', b, ":", bin(b))
print('a & b = ', a & b, ":", bin(a & b))
print('a | b = ', a | b, ":", bin(a | b))
print('a ^ b = ', a ^ b, ":", bin(a ^ b))
print('~a = ', ~a, ":", bin(~a))
a = 0b1
print('a = ', a)
a = a << 1 # * 2 
print('a = ', a)
a = a << 1 # * 2
print('a = ', a)
a = a << 3 # * 2**3
print('a = ', a)
a = a >> 1 # / 2
print('a = ', a)
a = a >> 1 # / 2
print('a = ', a)
a = a >> 2 # / 2**2
print('a = ', a)


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')
print()

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라")

# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: 
    print("택시를 타고가라")
else:
    print("걸어가라")

# 조건문 한줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")


# 조건부 표현식
score = 95
message = "success" if score >= 60 else "failure"
print(message)
# 조건부 표현식은 다음과 같이 정의한다.
# 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값