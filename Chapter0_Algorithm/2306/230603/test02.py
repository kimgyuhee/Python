"""
XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다. 
XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다. 
할인하는 제품은 하루에 하나씩만 구매할 수 있습니다. 
알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.

예를 들어, 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개이며, 
XYZ 마트에서 15일간 회원을 대상으로 할인하는 제품이 날짜 순서대로 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나인 경우에 대해 알아봅시다. 첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는 회원가입을 하지 않습니다. 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다. 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.

정현이가 원하는 제품을 나타내는 문자열 배열 want와 
정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, 
XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 
회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 
가능한 날이 없으면 0을 return 합니다.
"""

def solution(want, number, discount):
    answer = 0
    day = 0
    
    for i, d in enumerate(discount) :
        print("-"*100)
        n = number.copy()
        print(n)
        print(i)
        if len(discount[i:]) < sum(number) :
            break

        while day != 10 :

            print(discount[i+day])
            try :
                idx = want.index(discount[i+day])
                if n[idx] != 0 :
                    n[idx] -=1
            except ValueError :
                print("에러 발생")
                continue
            finally :
                day +=1
        if sum(n) == 0 :
            answer +=1
        day = 0

    return answer


# 다른 사람 풀이 1
def solution(want, number, discount):
    answer, wants = 0, []
    for v, n in zip(want, number):
        wants += [v]*n
    wants = sorted(wants)
    for i, product in enumerate(discount[:-len(wants)+1]):
        if product in wants:
            if wants == sorted(discount[i:len(wants)+i]):
                answer += 1

    return answer

# 다른 사람 풀이 2
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer
"""
채점 결과
정확성: 75.0
합계: 75.0 / 100.0
>>> 시간초과
접근 방식이 잘못되었다.
"""
def solution(want, number, discount):
    answer = 0
    day = 0
    
    for i, d in enumerate(discount) :
        n = number.copy()
        if len(discount[i:]) < sum(number) :
            break

        while day != 10 :
            try :
                idx = want.index(discount[i+day])
                if n[idx] != 0 :
                    n[idx] -=1
            except ValueError :
                continue
            finally :
                day +=1
        if sum(n) == 0 :
            answer +=1
        day = 0

    return answer


def solution(want, number, discount):
    answer = 0
    day = 0
    
    for i, d in enumerate(discount) :
        n = number.copy()
        if len(discount[i:]) < sum(number) :
            break

        while day != 10 :
            try :
                idx = want.index(discount[i+day])
                if n[idx] != 0 :
                    n[idx] -=1
            except ValueError :
                continue
            finally :
                day +=1

        if sum(n) == 0 :
            answer +=1
        day = 0

    return answer



print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))

l = [1, 2, 3, 4, 5, 6, 7, 0, 8, 9]
print(l[1:1+110]) # 에러 발생안함