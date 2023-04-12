"""
평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어 졌고 고민 끝에 카카오 TV 라이브로 방송을 하기로 마음먹었다.

그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 아래와 같이 독특한 방식을 생각해냈다.

회전판에 먹어야 할 N 개의 음식이 있다.
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다.
무지는 다음과 같은 방법으로 음식을 섭취한다.

무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.
무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다.
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.
"""

def solution(food_times, k):
    def findFalse(food_eat, index) :
        #print(food_eat)
        meet = 1
        for f in food_eat :
            if not food_eat[(index+1)%len(food_eat)] :
                meet +=1
                break
        #print(">>>>" ,meet)
        return meet%len(food_eat)
    

    food_eat = [False for _ in range(len(food_times))]
    meetZero = 0
    for i in range(k) :
        if sum(food_times) == 0 :
            break
        nowIndex = (i+meetZero)%len(food_times)
        #print(nowIndex)
        if food_times[nowIndex] != 0 and not food_eat[nowIndex]:
            #print("들어왔어요")
            food_times[nowIndex] -= 1
            #print(food_times)
            #print(food_eat)
        else : # 0 일때
            food_eat[nowIndex] = True
            meetZero += findFalse(food_eat, nowIndex)
            ii = (i+meetZero)%len(food_times)
            # print(f"nowIndex({nowIndex}) ->> food_times[{ii}] :{food_times[ii]}")
            food_times[ii] -= 1

    print(food_times)
    # print(food_times)
    if sum(food_times) == 0 :
        return -1
    else :
        return nowIndex

import heapq as hq

def solution(food_times, k) :
    # food_times의 합이 k보다 작거나 같을 경우 -1
    if sum(food_times) <=k : # 즉 음식은 마지막까지 무조건 남게 된다
        return -1
    
    foods = [] # food_times를 대신할 리스트
    print(food_times)
    for idx, food in enumerate(food_times) :
        hq.heappush(foods, (food, idx)) # heap 방식으로 (food, idx)를 요소로 가짐
        print(f">>>> foods : {foods}\n(food, idx) : ({food}, {idx})")
        # print(f"hq : {hq}")
    
    N, bef = len(foods), 0
    for _ in range(N) :
        print("\n\n다른 반복문 들어왔어요")
        food, idx = hq.heappop(foods) # food 값이 제일 작은 것을 pop
        print(f">>>> foods : {foods}\n(food, idx) : ({food}, {idx})")
        k -= ((food -bef) * N) # 남은 food의 값
        print("남은 음식의 값 : ", k)
        if k <=0 :
            print("\n\n조건문 들어왔어요 :)")
            hq.heappush(foods, (food, idx))
            print(f">>>> foods : {foods}\n(food, idx) : ({food}, {idx})")
            k +=((food-bef) * N)
            print("남은 음식의 값 : ", k)
            break
        bef = food
        N -=1

        print(f"bef : {bef}, N : {N}")

    foods.sort(key=lambda x : x[1])
    k = k % N
    print(foods, ">>>>> ",k)
    return foods[k][1]+1


print(solution([1, 1, 5, 7, 8], 11))
print(solution([4, 1, 5, 7, 8], 11))
print(solution([1, 1, 7], 6))
print(solution([3, 1, 2], 5))
print(solution([3, 1, 2], 6))