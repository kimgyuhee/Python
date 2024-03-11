# 그냥 운이다...
import random

lotto = []
while(len(lotto)!=6) :
    num = random.randint(1,45)
    if num not in lotto :
        lotto.append(num)

while(True) :
    bonus = random.randint(1,45)
    if bonus not in lotto :
        break


output = "1 2 3 4 5 6"
num_list = list(map(int, output.split(" ")))
count = 0
score = ""
for num in num_list :
    if num in lotto :
        count +=1

if count == 6 :
    score = "100점"
elif count == 5 :
    if bonus in num_list :
        score = "80점"
    else :
        score = "60점"
elif count == 4 :
    score = "40점"
elif count == 3 :
    score = "20점"
else :
    score = "틀렸습니다"

print(output)
# print(score)



