"""
https://wikidocs.net/194546
08-02. Heapify 구현하기

주어진 배열(리스트)이나 이진트리를 힙 구조로 재배열하는 것을 heapify라 한다. 
앞서 만든 마지막 예제처럼 힙 구조로 만들 배열의 원소를 차례로 heappush해서 힙 구조의 배열을 별도로 만드는 것은 쉽다.

그 코드를 다시 살펴보자.

"""

import heapq

def heapify(arr):
    current = start = len(arr)-1
    while start > 0:
        is_swaped = False
        while current > 0:
            parent = (current - 1) // 2
            if arr[parent] > arr[current]:
                arr[parent], arr[current] = arr[current], arr[parent]
                current = parent
                is_swaped = True
            else:
                break
        if is_swaped:
            current = start
        else:
            current = start = current - 1

h = []
arr = [21, 33, 17, 27, 9, 11, 14]
heapq.heapify(h)
for i in arr:
    heapq.heappush(h, i)

print(h) # [9, 17, 11, 33, 27, 21, 14]
"""
테스트하기
테스트 1

실행 결과는 아래와 같다. 파이썬의 heapq 모듈과 결과를 비교했다.

"""
h1 = [5, 2, 4, 1, 3]
h2 = [5, 2, 4, 1, 3]
heapq.heapify(h1) #내장 모듈의 함수를 이용한 것
heapify(h2)
print(h1)
print(h2)
# 결과가 같다.

"""
테스트 2

배열의 값을 바꾼 후 실행한다.
이번에는 결과가 다르다. 순서는 다르지만 직접 구현한 함수로 실행한 결과도 힙이다.
"""
h1 = [3, 4, 5, 1, 2]
h2 = [3, 4, 5, 1, 2]
heapq.heapify(h1) #내장 모듈의 함수를 이용한 것
heapify(h2)
print(h1)
print(h2)
# 결과가 다르다.

"""
테스트 3

>>> import heapq
>>> h1 = [1, 5, 6, 4, 3, 8, 7, 2]
>>> h2 = [1, 5, 6, 4, 3, 8, 7, 2]
>>> heapq.heapify(h1)
>>> heapify(h2)
>>> print(h1)
[1, 2, 6, 4, 3, 8, 7, 5]
>>> print(h2)
[1, 2, 6, 4, 3, 8, 7, 5]
이 외에도 여러 사례를 대입한 결과는 모두 힙 구조였다. 
하지만, 뭔가 맘에 안 들고 개선할 점이 더 있을까 해서 코드를 이렇게 저렇게 수정했지만, 
좋은 결과를 얻지 못했다.
"""


def heapify2(arr):
    last = len(arr) // 2 - 1
    for current in range(last, -1, -1):
        while current <= last:
            child = current * 2 + 1
            sibling = child + 1
            if sibling < len(arr) and arr[child] > arr[sibling]:
                child = sibling
            if arr[current] > arr[child]:
                arr[current], arr[child] = arr[child], arr[current]
                current = child
            else:
                break


def max_heapify(arr):
    last = len(arr) // 2 - 1
    for current in range(last, -1, -1):
        while current <= last:
            child = current * 2 + 1
            sibling = child + 1
            if sibling < len(arr) and arr[child] < arr[sibling]:
                child = sibling
            if arr[current] < arr[child]:
                arr[current], arr[child] = arr[child], arr[current]
                current = child
            else:
                break

