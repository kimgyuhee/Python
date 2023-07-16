"""
주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 
차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.

기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
180           5000	       10	       600
"""
import math
def time_calculator(time1, time2) :
    hour1, minute1 = time1.split(":") # in-time
    hour2, minute2 = time2.split(":") # out-time

    hour = int(hour2)- int(hour1)
    if int(minute1) > int(minute2) :
        minute = (60+int(minute2)) - int(minute1)
        hour -=1
    else :
        minute = int(minute2)-int(minute1)

    print(hour1, hour2, hour)
    return hour*60+minute

    
def solution(fees, records):
    answer = []
    time_memory = {}
    for r in records :
        time, car_id, in_out = r.split(" ")
        if car_id in time_memory :
            time_memory[car_id].append(time)
        else :
            time_memory[car_id] = [time]

    time_memory = dict(sorted(time_memory.items(), reverse=False))
    print(time_memory)
    for i in time_memory :
        interval = 0
        if len(time_memory[i])%2 == 1 :
            time_memory[i].append('23:59')

        for n in range(0,len(time_memory[i]), 2) :
            interval += time_calculator(time_memory[i][n], time_memory[i][n+1])

        print(interval)
        if interval < fees[0] :
            result = fees[1]
        else :
            result = fees[1] + math.ceil((interval-fees[0])/fees[2]) * fees[3]
        answer.append(result)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))