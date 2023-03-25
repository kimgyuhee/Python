"""
클래스(class)
- C 언어에는 클래스가 없다.
과자 틀 → 클래스 (class)
과자 틀에 의해서 만들어진 과자 → 객체 (object)

클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 가진다는 것이다.
"""

"""
객체와 인스턴스의 차이
클래스로 만든 객체를 인스턴스라고도 한다.
a = Cookie() 이렇게 만든 a는 객체이다.
그리고 a 객체는 Cookie의 인스턴스이다.
즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
"a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며
"a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.
"""

class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
    
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self라는 이름를 사용한 것이다

class FourCal() :

    # 생성자
    # def __init__(self) -> None:
    #     pass   

    def __init__(self, a, b) : #self : 생성되는 객체
        self.a = a
        self.b = b      

    def setDate(self, a, b) :
        self.a = a
        self.b = b

    def add(self) :
        return self.a + self.b
    
    def mul(self) :
        return self.a * self.b
    
    def sub(self) :
        return self.a - self.b
    
    def div(self) :
        return self.a / self.b
    
    def print(self) :
        print(f"### {self.a}와 {self.b}의 사칙연산 결과 ###")
        print(self.add())
        print(self.mul())
        print(self.sub())
        print("%0.2f" %self.div())
    

# test1 = FourCal()
# test2 = FourCal()
# test1.setDate(4, 2)
# test2.setDate(3, 7)

# test1.print()
# test2.print()

test3 = FourCal(3, 24)
test3.print()

test4 = FourCal(3, 5)
test4.print()

# 클래스의 상속
class MoreFourCal(FourCal):
    
    def pow(self) :
        return self.a ** self.b
    
    # 오버라이딩
    def div(self) :
        if(self.b == 0) :
            return 0
        else :
            return self.a / self.b
        
    # 오버라이딩
    def print(self):
        super().print()
        print(self.pow())

a = MoreFourCal(4, 2)
a.print()
print(a.pow())

b = MoreFourCal(4, 0)
b.print()

"""
왜 상속을 해야 할까?

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.

메서드 오버라이딩(Overriding, 덮어쓰기)
- 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
- 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출
"""

# 클래스 변수
class Family:
    lastname = "김"
    blood = "O형"

print(Family.lastname)
print(Family.blood)

f1 = Family()
f2 = Family()
print("{0:=^20}".format("변경전"))
print(f1.lastname, f1.blood)
print(f2.lastname, f2.blood)

# Family 클래스의 변수를 값을 변경하면?
print("{0:=^20}".format("변경후"))
Family.lastname = "박"
Family.blood = "A형"
print(f1.lastname, f1.blood)
print(f2.lastname, f2.blood)

# f2객체 Family 안스턴스의 변수를 값을 변경하면?
print("{0:=^20}".format("변경후"))
f2.lastname = "강"
f2.blood = "AB형"
print(f1.lastname, f1.blood)
print(f2.lastname, f2.blood)
