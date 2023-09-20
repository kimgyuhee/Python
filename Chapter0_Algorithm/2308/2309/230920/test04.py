#2309/230920/test03.py 채점 코드
#채점 결과
#정확성: 13.3
#효율성: 0.0
#합계: 13.3 / 100.0


def solution(works, n):
    answer = 0
    time = n
    if sum(works) <= n :
        return 0
    else :
        intervals = []
        works_sort = sorted(works)

        interval_sum = 0
        for i in range(len(works_sort)-1) :
            interval = works_sort[i] - works_sort[i+1]
            interval_sum +=interval
            intervals.append(abs(interval_sum))
        
        intervals.reverse()
        for i in range(len(intervals)-1) :
            print(i)
            print(f"""
==============================
{i}번째 인덱스에 대해 차이 값을 줄이고 있습니다.               
{intervals}
{time}
==============================
""")
            if time == 0 or sum(intervals) == 0 : # 종료될 수 있는 조건
                break

            if intervals[i] > intervals[i+1] :
                sub = intervals[i]- intervals[i+1]
                if time > sub :
                    time -=sub
                    intervals[i] -= sub
                    works_sort[len(works_sort)-i-1] -=sub
            
            #print(">>>", works_sort)
            if intervals[i] == intervals[i+1] and intervals[i]!=0 and time!=0:
                # print("안들어오나요 ?")
                while time != 0 :
                    if len(intervals) > 2 and len(intervals) != i+1 :
                        if intervals[i+1] == intervals[i+2] :
                            break
                    print(intervals)
                    print(">>>", works_sort)
                    print("\n", time)
                    if time == (i+1) :
                        works_sort[len(works_sort)-i-1] -=1
                        intervals[i] -= 1
                        time-=1
                        break
                    else :
                        works_sort[len(works_sort)-i-1] -=1
                        works_sort[len(works_sort)-i-1-1] -=1
                        intervals[i] -= 1
                        intervals[i+1] -= 1
                        time-=2
            # break
    for n in range(time) :
        time-=1
        works_sort[n%len(works_sort)] -=1
    
    for work in works_sort :
        answer += work**2
    return answer


from heapq import heapify, heappush, heappop

def solution(works, n):
# def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [(-1) * work for work in works]
    heapify(works)
    while n:
        print(n)
        print(">>>", works)
        curr_work = heappop(works)
        print(">>> heappop", works)
        post_work = curr_work + 1
        print(">>> post_work : ", post_work)
        heappush(works, post_work)
        print(">>> heappush", works)
        n -= 1

    return sum([work ** 2 for work in works])

print(solution([10, 4, 4, 7, 1, 4, 3, 3], 10)) # 27 + 1 + 64 = 92
print("="*27)
print(solution([30, 47, 1, 9, 10, 1, 1 ,15, 20],72)) # 37+20+10+5 = 72
# 500 + 81 + 3