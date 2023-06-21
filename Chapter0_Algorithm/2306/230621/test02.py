"""
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 
아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 
원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 
return 하도록 solution 함수를 작성해주세요.
"""

from collections import deque
def solution(scoville, K):
    answer = 0
    now_scov = 1
    while min(scoville) <= K :
        answer +=1
        scoville = deque(scoville)
        scoville.sort()
        first_score = scoville.popleft()
        second_score = scoville.popleft()
        mix_score = first_score + (second_score * 2)
        scoville.append(mix_score)
    return answer


# 채점 결과
# 정확성: 71.0
# 효율성: 0.0
# 합계: 71.0 / 100.0
def solution(scoville, K):
    answer = 0
    while min(scoville) <= K :
        if len(scoville) <= 1 :
            return -1
        answer +=1
        scoville.sort()
        # print(scoville)
        first_score = scoville[0]
        second_score = scoville[1]
        scoville.remove(first_score)
        scoville.remove(second_score)
        mix_score = first_score + (second_score * 2)
        scoville.append(mix_score)
    return answer




import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    print(scoville)
    while scoville[0] <= K :
        if len(scoville) <= 1 :
            return -1
        answer +=1
        first_score = heapq.heappop(scoville)
        second_score = heapq.heappop(scoville)
        mix_score = first_score + (second_score * 2)
        heapq.heappush(scoville, mix_score)
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))