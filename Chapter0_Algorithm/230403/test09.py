"""
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 
해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 
제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 
제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.


0 1 2 index-3
3 4 5
6 7(2*3)+1 8()
"""

# 65점 코드
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    stack = deque()

    if cacheSize == 0 :
        return len(cities) * 5
    
    for city in cities :
        city = city.lower()
        if city not in stack :
            if len(stack) < cacheSize:
                answer +=5
                stack.append(city)
            else :
                answer +=5
                stack.popleft()
                stack.append(city)
        else :
            """
            저 두줄을 추가하면 점수 받을 수 있었음,,,
            """
            stack.remove(city) ##############################
            stack.append(city) ##############################
            answer +=1
    return answer

# 75점 코드
def solution(cacheSize, cities):
    answer = 0
    stack = deque()
    nowIndex = 0
    if cacheSize == 0 :
        return len(cities) * 5
    
    for city in cities :
        city = city.lower()
        if city not in stack :
            if len(stack) >= cacheSize :
                value = stack[nowIndex]
                stack.remove(value)
            answer +=5
            stack.append(city)
        else :
            answer +=1
            nowIndex = (nowIndex+1)%cacheSize
    return answer


def solution(cacheSize, cities):
    answer = 0
    stack = deque()
    nowIndex = 0
    oldCity = ""

    if cacheSize == 0 :
        return len(cities) * 5
    
    for city in cities :
        city = city.lower()
        if city not in stack :
            if len(stack) >= cacheSize :
                oldCity = stack[nowIndex]
                stack.remove(oldCity)
                nowIndex = 0
            answer +=5
            stack.append(city)
        else :
            answer +=1
            nowIndex +=1
    return answer


# 100점 코드,,, 결국 구글링
def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5

    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(1, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "LA"]))
print(solution(3, ["a", "b", "c", "a"]))
print(solution(3, ["a", "b", "c", "a", "b"]))
print(solution(3, ["a", "b", "c", "a", "b", "d", "c"]))