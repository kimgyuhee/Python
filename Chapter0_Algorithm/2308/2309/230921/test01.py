"""
참조: 프로그래머스 > 더 맵게
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 
Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다. 
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해 주세요.

제한 사항

scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

scoville = [1, 2, 3, 9, 10, 12], K = 7
return = 7
"""

import heapq
def solution(scoville, K) :
    answer = 0
    s = scoville[:]
    heapq.heapify(s)
    print("="*20)
    for i in s :
        print(i)
    print("="*20)
    while s and s[0] < K :
        try :
            new_food = heapq.heappop(s) + heapq.heappop(s) * 2
            heapq.heappush(s, new_food)
            answer += 1
        except :
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([5, 4, 10, 23, 43, 1, 19, 8, 33], 1))


s = [5, 4, 10, 23, 43, 1, 19, 8, 33]
heapq.heapify(s)
print(s)
while s :
    print("들어왔내구")
    print(heapq.heappop(s))


import heapq

def solution(works, n) :
    if sum(works) <= n:
        return 0
    
    works = [(-1) * work for work in works]
    heapq.heapify(works)
    while n :
        max_value = heapq.heappop(works)
        max_value +=1
        heapq.heappush(works, max_value)
        n -=1

    return sum([work **2 for work in works])


print(solution([4, 3, 3], 4)) # 12
print(solution([2, 1, 2], 1)) # 6
print(solution([10, 4, 4, 7, 1, 4, 3, 3], 10)) # 27 + 1 + 64 = 92
print("="*27)
print(solution([30, 47, 1, 9, 10, 1, 1 ,15, 20],72)) 