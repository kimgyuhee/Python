"""
프로그래밍 기초, 문자열
문자열은 그 요소값을 변경할 수 없다.
그래서 immutable한 자료형
* int, string, tuple(튜플)
여기에 속한 객체들은 call by value 속성
VS
mutable한 자료형
list(리스트), dict(딕셔러니)
call by reference 속성
"""

food = "Python's favorite food is perl"

array = food.split()
l = list(food)
print(l)
print(array)

print("삑소리가 날까나?????\a")
print("쳇 안나는듯해? \b\b\b m널문자??  \000 오호라 신나는군 \n \t \\000  ")

# 문자열 더해서 연산하기
head = "Python "
tail = "is fun!"
print(head + tail)
print(head * 2 ) # 문자열 곱하기
print("="*50)
print(len(head)+ len(tail)) #문자열 길이 구하기

a = "Life is too short, You need Python"
num = 0
empty = 0
small = 0 
big = 0
what = 0 

for i in a :

    if ord(i) >= ord('a') and ord(i) <= ord('z') :
        small +=1
    elif ord(i) >= ord('A') and ord(i) <= ord('Z') :
        big +=1
    elif i == " " : # 띄어쓰기 갯수 구하기
        empty +=1
    else :
        what +=1



    print(f"a[{num}] = {i} -> 아스키 코드 : {ord(i)}")
    num +=1


print(f"{a}의 총 글자 갯수 : {len(a)}")
print(f"{a}의 공백 갯수 : {empty}")
print(f"{a}의 소문자 갯수 : {small}")
print(f"{a}의 대문자 갯수 : {big}")
print(f"{a}의 특수기호 갯수 : {what}")

print(ord("A"), ord("a"), ord("Z"), ord('z'))
print(type(ord("a")))
print(chr(45), chr(96))

print(a[0:4]) # 문자열 슬라이싱
print(a[-6:])
print(a[5:-6])

ta = "a"
tb = "a"

print(ta == tb)

ta = (1, 2)
tb = (1, 2) + (3,)
tc = (3,) #tuple
td = (3) #int
print(tb)
print(type(tc))
print(type(td))

print("="*50)

la = [1,2]
lb = [1,2]
print(la == lb)
la = lb
la.append(4)
print(la == lb)



da = {1 : 'a'}
db = {2 : 'b'}
print(da)
print(db)

da[2] = 'b'
print(da)


number = 4
아침 = "I eat %d apples" %number
print(아침)

number = 10
day = "three"
aaa = "I ate %d apples. so I was sick for %s days." % (number, day)

print(aaa)

print("65의 아스키 코드는 ? %c" %65)
print("65의 8진수는 ? %o" %65)
print("65의 16진수는 ? %x" %65)

# 정렬과 공백
"""
%10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을
오른쪽으로 정렬하고 나머지는 공백으로 남겨 두라는 의미
"""
print("%10s" %"hi") 
print("%-10sjane" %"hi")

# 소수점 표현하기
print("%0.4f" %3.532343432) 

print("%10.4f" %3.4231234)

#format 함수를 사용한 포메팅
print("I eat {0} apples.".format(3))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

#왼쪽 정렬
leftSort = "{0:<10}".format("hi")
leftSortf = f'{"hi":<10}'
print(leftSort)
print(leftSortf)

#오른쪽 정렬
rightSort = "{0:>10}".format("hi")
print(rightSort)

#가운데 정렬
middleSort = "{0:^10}".format("hi")
print(middleSort)

#공백채우기
middleSort1 = "{0:=^10}".format("hi")
middleSort2 = f"{'hi':=^10}"
print(middleSort1)
print(middleSort2)

print("{{ and }}".format())