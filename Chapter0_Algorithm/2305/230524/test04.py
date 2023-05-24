"""
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

1. 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
2. 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 
(10 × p + q)2 점을 얻습니다.
3. 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 
(p + q) × |p - q|점을 얻습니다.
4. 어느 두 주사위에서 나온 숫자가 p로 같고 
나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
5. 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 
얻는 점수를 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, b, c, d):
    answer_list = [a, b, c, d]
    # 주사위가 각각 나온 횟수를 저장하기 위한 코드
    box = [[0, i+1] for i in range(6)]
    for a in answer_list :
        box[a-1][0]+=1
    
    box.sort(reverse=True)

    # 각 경우의 수의 결과를 반환하는 조건문
    if box[0][0] == 4 :
        return 1111*box[0][1]
    elif box[0][0] == 3 :
        return (10*box[0][1]+box[1][1])**2
    elif box[0][0] == 2 :
        if box[1][0] == 2 :
            return (box[0][1]+box[1][1])*abs(box[0][1]-box[1][1])
        else :
            return box[1][1]*box[2][1]
    else :
        return box[3][1]

print(solution(2, 2, 2, 2))