"""
인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 
그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!

치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
"""

scores = {"A+": 4.5, "A0" : 4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0}

n = 20
sum = 0.0
total_credits = 0.0

for i in range(20):
    subject = input().split(" ")

    if subject[2] == "P":
        n -=1
    elif subject[2] == "F":
        total_credits += float(subject[1])
    else :
        total_credits += float(subject[1])
        a = scores[subject[2]]
        b = float(subject[1])
        sum+=(a*b)


# print(sum)
# print(total_credits)
# print(n)
result = sum / total_credits
print(round(result, 6))