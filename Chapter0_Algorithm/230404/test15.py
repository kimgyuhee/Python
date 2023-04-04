"""
import heapq as hq

우선순위 큐
우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용합니다.

자료구조 - 추출되는 데이터
스택(Stack) - 가장 나중에 삽입된 데이터
큐(queue) - 가장 먼저 삽입된 데이터
우선순위 큐 - 우선 순위가 높은 데이터

구현방식  삽입 / 삭제
리스트  O(1) / O(N)
힙  O(logN) / O(logN)

* 완전 이진 트리 형식이다.
"""
import heapq as hq
from heapq import heappush

heap = []
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
print(heap)

from heapq import heappop

print(heappop(heap))
print(heap)
print(heappop(heap))
print(heap)
print(heappop(heap))
print(heap)

h = [4,5,1,6,5]
hq.heapify(h)
print(h)
print(heappop(h))
print(h)


# 기존 리스트를 힙으로 변환
from heapq import heapify

heap = [4, 1, 7, 3, 8, 5]
heapify(heap)
print(heap)

"""
heapq 모듈은 최소 힙(min heap)을 기능만을 동작하기 때문에 
최대 힙(max heap)으로 활용하려면 약간의 요령이 필요합니다. 
바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 
튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.

따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, 
(우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 됩니다. 
그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됩니다. 
(우선 순위에는 관심이 없으므로 )
"""
from heapq import heappush, heappop

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heappush(heap, (-num, num))  # (우선 순위, 값)
  print(f"heap : {heap}")

while heap:
  print(heappop(heap)[1])  # index 1