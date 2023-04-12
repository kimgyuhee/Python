"""
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(dots):
    # CASE는 총 3개이다.
    case = { "CASE1" : [0,1,2,3], "CASE2" :[0,2,1,3], "CASE3" : [0,3,1,2]}
    """
    1 2 / 3 4
    1 3 / 2 4
    1 4 / 2 3
    """
    answer = 0
    for b, c in case.items() :
        # print(c[0])
        if abs(dots[c[0]][0] - dots[c[1]][0]) == abs(dots[c[2]][0] - dots[c[3]][0]) and abs(dots[c[0]][1] - dots[c[1]][1]) == abs(dots[c[2]][1] - dots[c[3]][1]) :
            answer = 1
            break
            
    return answer

## 위에 코드는 완벽하지 않은 코드

def solution1(dots):
    answer = 0
    dots_idx = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 2, 0, 3]]
    for d1, d2, d3, d4 in dots_idx:
        x1, y1 = dots[d1][0], dots[d1][1]
        x2, y2= dots[d2][0], dots[d2][1]
        x3, y3= dots[d3][0], dots[d3][1]
        x4, y4= dots[d4][0], dots[d4][1]
        if (y1-y2)*(x3-x4) == (y3-y4)*(x1-x2) :
            answer = 1
    return answer

def solution2(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0
