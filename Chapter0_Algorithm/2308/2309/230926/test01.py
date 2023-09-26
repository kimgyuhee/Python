import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    #print(q)
    current_time, total_response_time = 0, 0

    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr

        while len(tasks) > 0 and tasks[0][1] <= current_time:
            #print(tasks[0], tasks[0][1], current_time)
            #print("들어옴1 ?", q, tasks)

            heapq.heappush(q, tasks.popleft())

            # print("들어옴2 ?", q, tasks, tasks[0], current_time, "\n")

        if len(tasks) > 0 and len(q) == 0:

            #print("들어옴3 ?", q, tasks)

            heapq.heappush(q, tasks.popleft())

            # print("들어옴4 ?", q, tasks)

    return total_response_time // len(jobs)

print(solution([[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]]))
print(solution([[0, 3], [1, 9], [2, 6]]))


# 최대힙
import heapq

heap = []
values = [1,5,3,2,4]

# 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
for value in values:
	heapq.heappush(heap, -value)

# 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
for i in range(5):
	print(-heapq.heappop(heap))