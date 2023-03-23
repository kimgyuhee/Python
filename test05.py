"""
리스트 자료형

"""

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
f = list()

g = [a, b, c, d, e, f]
strFormat = "%-30s %-10s\n"
strOut = strFormat % ('list', 'type')

for i in g :
    strOut += strFormat % (i, type(i))

print(strOut)

#리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)

#리스트 길이구하기
str1 = "abc"
print(len(a))
print(len(str1))

i = 1
print(str(1)+str(a[0])) #문자열 더하기

#리스트의 수정과 삭제
print(f"수정 전 : {a}")
a[2] = 4
print(f"수정 후 : {a}")

del a[1]
print(f"수정 후 : {a}")

print("{0:=^30}".format(" del 함수 이용해 리스트 요소 삭제하기 "))
a = [1, 2, 3, 4, 5, 6, 7]
print(f"수정 전 : {a}")
del a[:3]
print(f"수정 후 : {a}")

#리스트 요소 추가(append)
print(a)
a.append(1)
a.append([2, 3])
print(a)

del a[len(a)-1]
print(a)

#리스트 정렬(sort)
a.sort()
print(a)

#리스트 뒤집기(reverse)
a = ['a', 'y', 's', 'b']
a.sort()
a.reverse()
print(a)

#인덱스 반환(index)
print(a.index('b'))
# print(a.index('k')) 리스트에 존재하지 않으면 오류 발생

#리스트 요소 삽입(insert)
a = [1, 2, 3]
a.insert(len(a), 4)
print(a)

#리스트 요소 제거(remove)
a.remove(1) #인덱스가 아닌 리스트 요소값을 넣어준다
print(a) #요소값이 없으면 오류 발생

#리스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop()) #마지막 요소 값을 리턴하고 그 요소는 삭제
print(a)

#리스트에 포함된 X요소 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))
print(a.count(""))
print(a.count(4))

#리스트 확장(extend)
a = [1, 2, 3]
a.extend([6, 7])
print(a)
a.extend([4, 5, 6])
print(a)
a+=[9, 8]
print(a)
a.sort()
print(a)
# a.extend([4, 5])는 a+=[4, 5]와 동일하다