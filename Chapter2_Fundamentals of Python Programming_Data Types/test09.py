"""
자료형의 값을 저장하는 공간, 변수

파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다. 객체란 우리가 지금껏 보아 온 자료형의 데이터(값)와 같은 것을 의미


"""

from copy import copy


a = 1
b = "python"
c = [1,2,3]
# 변수를 만들 때는 위 예처럼 =(assignment) 기호를 사용한다.
# 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형의 타입을 지정하기 때문에 더 편리
"""
만약 위 코드처럼 a = [1, 2, 3]이라고 하면 [1, 2, 3] 값을 가지는 리스트 데이터(객체)가 자동으로 메모리에 생성되고 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 된다.
메모리란 컴퓨터가 프로그램에서 사용하는 데이터를 기억하는 공간이다.
"""

# immutable
a = (1, 2, 3)
aa = (1, 2, 3)
print(id(a))
print(id(aa))

print(a is aa)

# mutable
l = [1, 2, 3]
ll = [1, 2, 3]
print(id(l))
print(id(ll))

print(l is ll)

ll = l
print(l is ll)
print(id(l))
print(id(ll))
ll.append(4)
print(l)
print(ll)

ll[1] = 0
print(l)
print(ll)

# ll 변수를 생성할 때 l 변수의 값을 가져오면서 
# l와는 다른 주소를 가리키도록 만들수는 없을까? 
# 다음 2가지 방법이 있다.
"""
1. [:] 이용
2. copy 모듈 이용
>>> from copy import copy
>>> a = [1, 2, 3]
>>> b = copy(a)
"""
l = [1, 2, 3]
ll = l[:]

print(l)
print(ll)

ll.append(4)
print(l)
print(ll)

print("="*50)
l = [1, 2, 3]
ll = copy(l)

print(l)
print(ll)

ll.append(4)
print(l)
print(ll)

print("{0:=^40}".format("변수를 만드는 여러 가지 방법"))
# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a)
print(b)
print(a, b)

(aa, bb) = 'python', 'life'
print((aa, bb))
print(type((aa, bb)))
print(aa)
print(type(aa))
print(bb)