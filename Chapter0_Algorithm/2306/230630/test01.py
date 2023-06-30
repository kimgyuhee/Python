"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

"""
# 테스트 케이스만 신경쓴 문제해석 오류
def solution(prices):
    answer = []
    for i in range(len(prices)-1) :
        second = 0
        for j in range(i, len(prices)-1) :
            if prices[i] <= prices[j] :
                second +=1
            else :
                break
        answer.append(second)
    answer.append(0)
    return answer

def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        sec = 0
        for j in range(i, len(prices) - 1):
            if(prices[i] <= prices[j]):
                sec += 1
            else:
                break
        answer.append(sec)
    answer.append(0)
    return answer


def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            print("prices[i], prices[j]",prices[i], prices[j])
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
            print(answer)
    return answer

print("=============="*2)
print(solution([4, 3, 2, 1]))
print(solution([2, 2, 3, 1, 5]))
print(solution([1, 2, 3, 2, 3]))

"""
입출력 예 설명
1초의 주가는 1이며 1초부터 5초까지 총 4초간 주가를 유지했습니다.
2초의 주가는 2이며 2초부터 5초까지 총 3초간 주가를 유지했습니다.
3초의 주가는 3이며 4초의 주가는 2로 주가가 떨어졌지만 3초에서 4초가 되기 직전까지의 1초간 주가가 유지 된것으로 봅니다. 따라서 5초까지 총 1초간 주가를 유지했습니다.
4초의 주가는 2이며 4초부터 5초까지 총 1초간 주가를 유지했습니다.
5초의 주가는 3이며 5초 이후로는 데이터가 없으므로 총 0초간 주가를 유지했습니다.
"""