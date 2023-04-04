def solution(n, x1, y1, x2, y2):

    # 두 섬이 맞대고 있는지 확인하는 함수
    # 반환값 True/False
    def overlap(rect1, rect2) :
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])
    
    result = []
    connected = [False for _ in range(n)] # 섬들이 연결되었는지 확인하는 변수
    
    for a, b, c, d in zip(x1, y1, x2, y2) : # 각 섬의 꼭지점을 모아서 저장하기 위한 반복문
        result.append([a, b, c, d])

    value = 0
    for i in range(len(result)-1) :
        meet = overlap(result[i], result[i+1])
        if meet :
            connected[i] = True
            connected[i+1] = True

    connected2 = [True, True, True, False, True, True, False]
    connected = [True]
    connected2 = [True, True, True, True, False, False]
    connected2 = [False, False, False, False]
    answer = []
    value = 0
    count = 0
    for conti in connected :
        if conti :
            value +=1
            count +=1
            if len(connected) == count :
                for i in range(value) :
                    answer.append(value)
        else :
            if len(connected) >= count :
                for i in range(value) :
                    answer.append(value)
            answer.append(1)
            count +=1
            value = 0

    return answer

print(solution(4, [10,30,65,10], [15,40,40,70], [40,65,80,30], [40,60,70,90]))