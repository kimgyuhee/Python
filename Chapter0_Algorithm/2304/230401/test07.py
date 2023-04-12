"""
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리
1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 
전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

"""
# 46점 코드
def solution(brown, yellow) :
    answer = []
    sum = brown + yellow
    num = sum**0.5
    if str(num)[2:] == "0" :
        return [int(num), int(num)]
    else :
        b = int(num)
        for i in range(b+1, b+10) :
            if sum % i == 0 and i*b == sum :
                a = i
                answer.append(a)
                answer.append(b)
                break
            
        return answer


def solution(brown, yellow):
    total = brown + yellow   
    yolo = yellow
    i = 1 
    while True:
        if ((yolo + 2) * (i + 2)) == total: break
        i += 1
        yolo = int(yellow / i)
        
    return [yolo+2, i+2]

print(solution(10,2))
print(solution(24,24))
print(solution(8,1))
print(solution(16,2))
print("잉?")