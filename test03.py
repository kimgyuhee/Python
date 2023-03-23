"""
프로그래밍 기초, 문자열
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

