"""
표준 라이브러리
"""

# datetime.date
# datetime.date는 년, 월, 일로 날짜를 표현할 때 사용하는 함수

import datetime

print("{0:=^20}".format("datetime.date"))
day1 = datetime.date(2019, 12, 14)
day2 = datetime.date(2021, 6, 5)
today = datetime.date(2023, 3, 25)
print(day1)
print(day2)
print(today)

diff = today - day2
print(f"{day2}와 {today}의 일수 차이는 ? {diff}")

# 파이썬은 switch문이 존재하지 않는다.
day = {0 : "월요일", 1 : "화요일", 2 : "수요일", 3 : "목요일", 4 : "금요일", 5 : "토요일", 6 : "알요일"}
print("{0}은 {1}입니다.".format(today, day[today.weekday()]))
# print(day[1])

# time
print("{0:=^20}".format("time"))
import time

# 현재 시간을 실수 형태로 리턴하는 함수
print(time.time())

# time.time()이 리턴한 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수
print(time.localtime(time.time()))

# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수
print(time.asctime(time.localtime(time.time())))

# time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시
print(time.ctime())

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

t = time.strftime('%c', time.localtime(time.time()))
print(t)
st = t.replace(":", " ")

st = st.split(" ")
print(st)

for i in range(5):
    print(i)
    time.sleep(0.5)

print()
# math
import math
print("{0:=^20}".format(" math "))
print(math.gcd(60, 100, 80)) # 최대공약수
print(math.lcm(15, 25)) # 최대공배수

# random
import random
print("{0:=^20}".format(" random "))
print(random.random())
print(random.randint(1, 10))

def random_pop1(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number) # number -> index

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("random_pop 함수")
    while data: 
        print(random_pop1(data))

data = [1, 2, 3, 4, 5]

def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("random_pop 함수")
    while data: 
        print(data)
        print(random_pop2(data))

a =  [1, 2, 3, 4, 5]
print(random.sample(a, len(a)))
print()


print("{0:=^20}".format(" itertools "))
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))


print("{0:=^20}".format(" itertools.permutations -> 순열"))
import itertools
순열 = list(itertools.permutations(['1', '2', '3'], 2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
print(순열)
print()
print()

print("{0:=^20}".format(" itertools.combinations -> 조합"))
조합 = list(itertools.combinations(['1', '2', '3'], 2))
print(조합)

중복조합 = list(itertools.combinations_with_replacement(range(1, 4), 3))
print("중복조합")
for i in 중복조합 :
    print(i)

print(len(중복조합))

import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  # 15 출력
print(data)

num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)  # 8 출력


# operator.itemgetter
from operator import itemgetter
students1 = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students1, key=itemgetter(1))
print(result)

students2 = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
result = sorted(students2, key=itemgetter('age'))
print(result)
for i in result :
    time.sleep(0.5)
    print(i)


# operator.attrgetter()
print("{0:=^20}".format(" operator.attrgetter() "))
"""
students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면
다음처럼 attrgetter()를 적용하여 정렬
"""
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"이름 : {self.name} / 나이 : {self.age} / 등급 : {self.grade}"

students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

for i in students :
    print(i)

result = sorted(students, key=attrgetter('age'))
print(result)
for i in result :
    print(i)