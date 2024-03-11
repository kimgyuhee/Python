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
score = 0
for num in num_list :
    if num in lotto :
        count +=1

if count == 6 :
    score = 100
elif count == 5 :
    if bonus in num_list :
        score = 80
    else :
        score = 60
elif count == 4 :
    score = 40
elif count == 3 :
    score = 20
else :
    score = 0

print(lotto)
print(bonus)
print(num_list)

if count >=3 :
    print("score : ", score)
else :
    print("틀렸습니다.")


