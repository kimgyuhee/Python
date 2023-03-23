"""
문자열 관련 함수
"""

a = "Python is the best choice"

# 문자 개수 세기(count)
print(a.count('i'))
print(a.count('')) #26
print(len(a)) #25

num = 0
for i in a :
    num+=1
    print(f'{num}번째 -> {i:>2}')

#위치 알려주기1(find)
print(a.find('P'))
print(a.find('k')) #문자열이 존재하지 않으면 -1 반환

#위치 알려주기2(index)
print(a.index('P')) # 만약 2개 이상 있다면 첫번째로 만난 인덱스 번호를 반환
# print(a.index('k')) 존재하지 않으면 오류 발생

#문자열 삽입(join)
print(",".join('abcd'))
array1 = ['a', 'b', 'c', 'd']
print(array1)
print(",".join(array1))

#소문자를 대문자로 바꾸기(upper)
b = a.upper()
print(a)
print(b)

#대문자를 소문자로 바꾸기(lower)
print(b)
print(b.lower())

#왼쪽 공백 지우기(lstrip)
a = "       hi"
print(a)
b = a.lstrip()
print(b)

#오른쪽 공백 지우기(rstrip)
a = "hi          "
print(a)
b = a.rstrip()
print(b)

#양쪽 공백 지우기(strip)
a = "           hi          "
aa = "{0:>20}".format("hi")
print(a)
print(aa)
print(aa.lstrip())
b = a.strip()
print(b)

#문자열 바꾸기(replace)
a = "Life is too short"
print(a)
aa = a.replace(a[:4], "Java")
print(aa)

#문자열 나누기(split)
aaa = a.split()
print(aaa)
print(type(aaa))

bbb = "a:b:c:d"
print(bbb.split(":"))