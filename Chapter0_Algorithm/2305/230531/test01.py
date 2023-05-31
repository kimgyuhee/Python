"""
수직선 상의 정수 점들 위에 n명의 사람들이 서있다. 
같은 위치에 여러 명이 있을 수도 있다. 
i번 사람의 수직선 상 위치를 A[i]라고 하자. 
또한 각 사람들은 왼쪽으로 최대 k칸, 
오른쪽으로 최대 k칸 움직일 수 있다. (움직이지 않을 수도 있다.)

사람들이 적절히 움직였을 때, 수직선에서 a 이상 b 이하의 구간에, 
사람들이 서있는 정수 점들의 가능한 최대 개수를 구하는 코드를 작성하시오.

"""

def solution(n, k, a, b, A):
    result = []
    
    for i in sorted(A) :
        if i >=a and i <=b :
            if i not in result :
                result.append(i)
            else :
                for j in range(k) :
                    if i-(j+1) >=a and i-(j+1)<=b :
                        if i-(j+1) not in result :
                            result.append(i-(j+1))
                            break
                    if i+(j+1) >=a and i+(j+1)<=b :
                        if i+(j+1) not in result :
                            result.append(i+(j+1))
                            break
    return len(result)


print(solution(5, 2, -1, 4, [4, 4, 4, 4, 4]))
print(solution(5, 1, -1, 4, [0, 1, 2, 4, 4]))
print(solution(5, 1, -1, 4, [0, 1, 2, 0, 4]))
print(solution(4, 2, 1, 4, [1, 2, 1, 2]))


def solution(n, k, a, b, A):
    result = []
    for i in sorted(A) :
        for j in range(k) :
            if i-(j+1) >=a and i-(j+1)<=b :
                if i-(j+1) not in result :
                    result.append(i-(j+1))
                    break
            if i+(j+1) >=a and i+(j+1)<=b :
                if i+(j+1) not in result :
                    result.append(i+(j+1))
                    break
    return len(result)