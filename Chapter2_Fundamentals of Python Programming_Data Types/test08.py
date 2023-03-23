"""
불 자료형
불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다. 불 자료형은 다음 2가지 값만을 가질 수 있다.
True - 참
False - 거짓
* True나 False는 파이썬의 예약어로 true, false와 같이 사용하지 말고 첫 문자를 항상 대문자로 사용해야 한다.
"""

print(1 == 1)
print(1 == 2)

if "python":
    print("참?")
else :
    print("거짓?")

if "": # [], (), {}, 0, None
    print("참?")
else :
    print("거짓?")

a = [1, 2, 3, 4]
while a :
    print(a.pop())

# Bool 연산
print(bool('python'))
print(bool(''))
print(bool('""'))