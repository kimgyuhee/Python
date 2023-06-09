"""
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 
만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, 
X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
"""

# 시간초과
# 합계: 73.7 / 100.0
def solution(X, Y):
    answer = ''
    countSet = {}
    for x in X :
        if x in Y and x not in countSet:
            countX = X.count(x)
            countY = Y.count(x)
            if countY != 0 :
                countSet[x] = min(countX, countY)
    
    if len(countSet) == 0 :
        answer = "-1"
    else :
        countSet_sort = sorted(countSet.items(), key=lambda x : x[0], reverse=True)
        print(countSet_sort[0][0])
        for c in countSet_sort :
            answer +=c[0]*c[1]
    
    if int(answer) == 0 :
        answer = "0"
    return answer



def solution(X, Y):
    answer = ''
    countSet = {}
    for x in X :
        if x in Y and x not in countSet:
            countX = X.count(x)
            countY = Y.count(x)
            if countY != 0 :
                countSet[x] = min(countX, countY)
            answer +=x*min(countX,countY)
            
    if answer == '' :
        answer = "-1"
    elif int(answer) == 0 :
        answer = "0"
    else :
        a = reversed(sorted(answer))
        answer = "".join(a)
    return answer


from collections import Counter
def solution(x,y):
    result = sorted(list((Counter((int(i) for i in x ))&Counter((int(i) for i in y ))).elements()), reverse=True)
    if result == []:
        return '-1'
    if result[0] == 0:
        return '0'
    return ''.join((str(i) for i in result))


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("5525", "1255"))