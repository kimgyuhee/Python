"""
집합 자료형
- 중복을 허용하지 않는다.
- 순서가 없다(Unordered).
"""

s1 = set([1,2,3])
print(s1)
print(type(s1))

s2 = set("Hello")
print(s2)

l1 = list(s1)
print(l1)
t1 = tuple(s1)
print(t1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print("{0:=^16}".format("교집합"))
print(f"s1 : {s1}")
print(f"s2 : {s2}")
print(f"s1 & s2 : {s1 & s2}")
print(f"s1.intersection(s2) : {s1.intersection(s2)}")

# 교집합
print("{0:=^16}".format("합집합"))
print(f"s1 : {s1}")
print(f"s2 : {s2}")
print(f"s1 | s2 : {s1 | s2}")
print(f"s1.union(s2)) : {s1.union(s2)}")

# 차집합
print("{0:=^16}".format("차집합"))
print("S1 - S2")
print(f"s1 : {s1}")
print(f"s2 : {s2}")
print(f"s1 - s2 : {s1 - s2}")
print(f"s1.difference(s2) : {s1.difference(s2)}")
print("S2 - S1")
print(f"s1 : {s1}")
print(f"s2 : {s2}")
print(f"s2 - s1 : {s2 - s1}")
print(f"s2.difference(s1) : {s2.difference(s1)}")

# 집합 자료형 관련 함수들
# 값 1개 추가하기(add)
print(s1)
s1.add(10)
print(s1)

# 값 여러개 추가하기(update)
print(s2)
s2.update([11, 12, 13, 1, 4, 6])
print(s2)

# 특정 값 제거하기(remove)
s2.remove(1)
print(s2)
# s2.remove([11, 12]) 하나씩만 가능
# print(s2)