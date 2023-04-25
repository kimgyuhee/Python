"""
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 
거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 
왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 
왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
"""
'''
L - R
1 2 3
4 5 6
7 8 9
* 0 #
'''

# 합계: 45.0 / 100.0
def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7]
    r = [3, 6, 9]
    c = [2, 5, 8, 0]
    left_finger = 0
    right_finger = 0
    for n in numbers :
        print(left_finger, right_finger, n, answer)
        if n in l :
            answer +="L"
            left_finger = n
        elif n in r :
            answer +="R"
            right_finger = n
        else :
            if left_finger in c :
                valueL = abs(c.index(left_finger)-c.index(n))
            else :
                valueL = abs(left_finger-n)
            if right_finger in c :
                valueR = abs(c.index(right_finger)-c.index(n))
            else :
                valueR = abs(right_finger-n)

            if valueL < valueR :
                answer +="L"
                left_finger = n
            elif valueL > valueR :
                answer +="R"
                right_finger = n
            else :
                if hand == "right":
                    answer+="R"
                    right_finger = n
                else :
                    answer +="L"
                    left_finger = n
    return answer


# 합계: 90.0 / 100.0
def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7, 10]
    r = [3, 6, 9, 12]
    c = [2, 5, 8, 0]
    left_finger = 10
    right_finger = 12
    for n in numbers :
        print(left_finger, right_finger, n, answer)
        if n in l :
            answer +="L"
            left_finger = n
        elif n in r :
            answer +="R"
            right_finger = n
        else :
            if left_finger in c :
                valueL = abs(c.index(n)-c.index(left_finger))
            else :
                valueL = abs(c.index(n)-l.index(left_finger))+1

            if right_finger in c :
                valueR = abs(c.index(n)-c.index(right_finger))
            else :
                valueR = abs(c.index(n)-r.index(right_finger))+1

            print(valueL, valueR)
            if valueR == valueL :
                if hand == "right" :
                    right_finger = n
                    answer +="R"
                elif hand == "left" :
                    left_finger = n
                    answer +="L"
            elif valueR > valueL :
                left_finger = n
                answer +="L"
            elif valueR < valueL :
                right_finger = n
                answer +="R"
    return answer

# 다른 사람 풀이
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print("LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print("LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
print("LLRLLRLLRL")