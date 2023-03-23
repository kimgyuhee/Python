print('Hello', end=" "); print('world')

"""
리스트
리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
괄호( )를 생략해도 된다
리스트는 요소 값의 생성, 삭제, 수정이 가능하지만 튜플은 요소 값을 바꿀 수 없다.

딕셔너리
파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형(딕셔너리)
이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.
딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다. 
"""
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
t6 = 1,

print(type(t6))

# 튜플은 요솟값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일

# 인덱싱 & 슬라이싱
print(t5[1])
print(t5[2])

print(t5[1:])

t7 = t3 + t5
print(t7)



dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}

strFormat = "%-10s %-10s\n"
strOut = strFormat % ('key', 'value')
strOut+="="*30+'\n'

keys = list(dic.keys())
values = list(dic.values())
print(keys)
print(values)
print("="*30)
for i in range(0, len(dic)) :
    if (i ==len(dic)-1) :
        strFormat = "%-10s %-10s"
    strOut += strFormat % (keys[i], values[i])

print(strOut)
print("="*30)

print(dic['name'])
print(dic['birth'])

print(dic)

#key값이 중복될 경우 마지막을 제외 무시된다
a = {1:'a', 1:'b', 1:'c'}
print(a)


"""
* dict의 Key값은 변하면 안된다. 그래서 리스트형은 올 수 없다.
튜플형은 가능 -> immutable 해야한다.
"""
print(a.keys())
print(a.values())

# dict_keys, dict_values 객체는 append, insert, pop, remove, sort 함수 사용 불가
# 위의 함수를 사용하려면 List형으로 변환해야한다. -> list(a)
for i in a.keys() :
    print(i)


# key, value 쌍 얻기(items())
dict_list = list(dic.items())
print(type(dict_list))

for i in dict_list :
    print(i[0])
    print(type(i))

# key: value 쌍 모두 지우기(clear)
a.clear()
print(a)
# 빈 리스트를 [], 빈 튜플을 ()로 표현하는 것과 마찬가지로 빈 딕셔너리도 {}로 표현한다.

# Key로 value얻기 (Get)
print(dic.get('name'))
print(dic.get('n')) # key 존재하지 않으면 None 
print(dic.get('n', 'nono')) # 첫번째 파라미터가 dic에 존재하지 않을때 두번째 파라미터 리턴
dic['home'] = 'Guri'
print(dic)

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in dic)
print('nn' in dic)