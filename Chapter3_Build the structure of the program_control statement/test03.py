"""
반복문 - for문
"""

# 전형적인 for문
test_list = ['one', 'two', 'three'] 
for i in test_list:
    print(i)

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# for문의 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.
exams = [95, 40, 25, 100, 80]
for e in exams :
    print(f"{e}점수는 ", end="")
    if(e >=60) :
        print("합격!")
    else :
        print("불합격")

marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a)
for i in a :
    print(i)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


# for와 range를 이용한 구구단
print("{0:=^30}".format("for와 range를 이용한 구구단"))
strFormat = "%15sx%s=%2s\n"
strOut = strFormat %("i", "j", "k")

for i in range(2, 10):
    for j in range(2, 10):
        strOut += strFormat %(i, j, i*j)

print(strOut)

for i in range(2, 10):
    for j in range(2, 10):
        print(f"{j}*{i}={j*i}", end="\t")
    print()

# 리스트 컴프리헨션 사용하기
a  = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result) # [3, 6, 9, 12]
######################
result1 = [num * 3 for num in a]
print(result1)

# 리스트 컴프리헨션 사용하여 구구단 출력하기

gugudan = [x*y for x in range(2,10) for y in range(1,10)]
print(gugudan)