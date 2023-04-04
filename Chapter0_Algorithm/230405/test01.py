"""
준원이는 게임을 만들고 있다. 게임에는 N개의 나라가 있다.

준원이는 각 나라의 영토를 나타내는 세계 지도를 그리고 있다. 세계 지도는 직사각형 모양이다. 
세계 지도 안에 있는 각 나라의 영토 또한 각 변이 세계 지도의 모서리와 평행한 직사각형 모양이다.

만약 두 나라의 영토가 서로 모서리를 맞대고 있다면, 
두 나라 사이를 걸어서 이동할 수 있다. 
서로 모서리를 맞대고 있지 않다면(꼭짓점만을 맞대고 있는 경우도 포함한다), 
두 나라 사이를 걸어서 이동할 수 없다.

준원이는 각 나라에 대해서, 다음과 같은 질문의 답을 계산해야 한다.

이 나라에서, 걸어서 방문할 수 있는 다른 나라의 개수는 몇 개일까? 
단, 다른 나라(들)를 경유해서 방문해야 하는 경우도 방문할 수 있다고 간주한다.

이 값을 모든 나라에 대해서 계산하라.


"""

def solution(n, x1, y1, x2, y2):
    # 두 섬이 맞대고 있는지 확인 하는 함수
    def overlap(rect1, rect2) :
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])
    
    answer = [0 for _ in range(n)]
    result = []
    connected1 = []
    connected2 = [False for _ in range(n)]
    for a, b, c, d in zip(x1, y1, x2, y2) :
        result.append([a, b, c, d])

    value = 0
    conti = True
    for i in range(len(result)-1) : 
        meet = overlap(result[i], result[i+1])
        if meet :
            value +=1
            answer[i]+=value
            answer[i+1]+=value
            connected1.append([i, i+1])
            connected2[i] = True
            connected2[i+1] = True
        else :
            conti = False
            value = 0


    connected2 = [True, True, True, False, True, True, False]
    connected2 = [False, True]
    connected2 = [True, True, True, True, False, False]
    connected2 = [False, False, False, False]
    answer2 = []
    value = 0
    count = 0
    for conti in connected2 :
        print(count, conti)
        if conti :
            value +=1
            count +=1
            if len(connected2) == count :
                for i in range(value) :
                    answer2.append(value)
        else :
            if len(connected2) >= count :
                for i in range(value) :
                    answer2.append(value)
            answer2.append(1)
            count +=1
            value = 0

    print(answer2)
    print(connected1)
    print(connected2)
    print(result)    
    return answer
# [3, 3, 3, 1]

print(solution(4, [10,30,65,10], [15,40,40,70], [40,65,80,30], [40,60,70,90]))