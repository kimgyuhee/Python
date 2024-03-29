"""
회사원 Demi는 가끔은 야근을 하는데요, 
야근을 하면 야근 피로도가 쌓입니다. 
야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. 
Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 
퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 
야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

"""
# 8 2 2 -> 4 2 2(24) 5 2 2 -> 1 2 2(9), 2 1 2

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
            #print(i)
            #print(intervals)
            if time == 0 or sum(intervals) == 0 : # 종료될 수 있는 조건
                break

            if intervals[i] > intervals[i+1] :
                sub = intervals[i]- intervals[i+1]
                if time > sub :
                    time -=sub
                    intervals[i] -= sub
                    works_sort[len(works_sort)-i-1] -=sub
            
            # print(">>>", works_sort)
            # print(intervals)
            if intervals[i] == intervals[i+1] and intervals[i]!=0 and time!=0:
                # print("안들어오나요 ?")
                while time != 0 :
                    if len(intervals) > 2 and len(intervals) != i+1 :
                        if intervals[i+1] == intervals[i+2] :
                            break
                    # print(intervals)
                    # print(works_sort)
                    if time == 1 :
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

print(solution([8, 8, 3, 3], 5)) # 6 6 3 3 / 8 4 3 3[36, 36, 9, 9] [64, 16, 9, 9]
print(solution([10, 8, 3, 3], 20)) # 7,7, 3, 3 / 8, 6, 3, 3 [49,49 / 64, 36]
print(solution([4, 3, 3], 4)) #12
print(solution([2, 1, 2], 1)) #6
print(solution([1, 1], 3)) #0