"""
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 
디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 
가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면
- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.


"""


from heapq import heappush, heappop, heapify

def solution(jobs):
    sum = 0
    wait_times = 0
    j = jobs[:]
    intervals = []
    heapify(intervals)
    heapify(j)
    start_value = heappop(j)
    wait_times = start_value[1]
    sum +=wait_times

    for job in j :
        if job[1] <= job[0] :
            work = job[1]
        else :
            work = abs(job[1]-job[0])

        heappush(intervals, [job[1], job[0], job[1]])

    while intervals:
        value = heappop(intervals)
        print(value)
        wait_times +=value[2]
        sum = sum + (wait_times - value[1])

    return sum//len(jobs)



def solution(jobs) :
    jobs.sort()
    time, candidates = 0, []

    for start, delay in jobs:
        while start >= time:
        #####
            d, s = heappop(candidates)
        #####
        else:
            heappush(candidates, [delay, start])

    while candidates:
        delay, start = heappop(candidates)
        #####

import heapq


def solution(jobs):
    n = len(jobs)
    # jobs 를 p_queue 로 변경 --> jobs 가 들어오는 순서대로 정렬된다.
    heapq.heapify(jobs)
    # 맨 처음꺼 꺼내보겠음 --> 젤 처음 시작하는게 나오겠지>?
    current, length = heapq.heappop(jobs)
    answer = 0
    pq = []
    # pq 라는 큐를 하나 더 사용해보겠음, 이건 현재 값에서 작업 길이를 추가한 걸로 정렬
    # 즉, 예측했을 때 결과 값을 오름차순
    # 맨처음 꺼를 pq에 넣어보겠음
    heapq.heappush(pq, (current + length, current, length))
    while pq:
        # pq에 있는 첫번째꺼(계산 값이 젤 작은 거)를 꺼냅니다.
        # current 는 선택한 작업이 끝난 시점
        current, start, length = heapq.heappop(pq)
        # answer 계산
        answer = answer - start + current
        while pq:
            # 여기 반복문은 pq를 비우고 jobs 에 채웁니다.
            _, c, d = heapq.heappop(pq)
            heapq.heappush(jobs, [c, d])
        while jobs:
            # jobs 에 남은 작업 중에 시작점이 current 보다
            # 작은 것들을 빼서 pq에 계산해서 넣어보겠슴
            if jobs[0][0] > current:
                # jobs 중 젤 작은게 current 보다 작아지면 반복문을 벗어나
                if not pq:
                    # 만약에 pq가 비었는데 jobs 는 존재할때,
                    # 즉, 도착한 작업이 없고 대기 작업은 존재할때
                    e, f = heapq.heappop(jobs)
                    heapq.heappush(pq, (e+f, e, f))
                break
            else:
                # current 보다 시작점이 작으면 가능한 경우이기 때문에 pq에 넣어봄
                a, b = heapq.heappop(jobs)
                heapq.heappush(pq, (current + b, a, b))

    answer /= n
    # 마무리

    return int(answer)
from heapq import heappush, heappop, heapify

def solution(jobs):
    sum = 0
    wait_times = 0
    j = jobs[:]
    intervals = []
    heapify(intervals)
    heapify(j)
    start_value = heappop(j)
    wait_times = start_value[1]
    sum +=wait_times

    for job in j :
        if job[1] <= job[0] :
            work = job[1]
        else :
            work = abs(job[1]-job[0])

        heappush(intervals, [job[1]+job[0], job[0], job[1]])

    while intervals:
        value = heappop(intervals)
        print(value)
        wait_times +=value[2]
        sum = sum + (wait_times - value[1])

    return sum//len(jobs)


print(solution([[0, 3]]))
print(solution([[0, 3], [1, 9], [2, 6]]))
# 3 / 8 / 4


print(solution([[2, 9], [3, 1], [7, 6], [9, 3]]))
print(solution([[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]])) #19

print(solution([[0, 3], [10, 1]] ))
print(solution([[7, 8], [3, 5], [9, 6]] ))
print(solution([[1, 4], [7, 9], [1000, 3]]))
print(solution([[0, 1], [2, 2], [2, 3]]))