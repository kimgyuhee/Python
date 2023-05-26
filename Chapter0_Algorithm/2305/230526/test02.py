"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
"""
"""
채점 결과
정확성: 36.4
합계: 36.4 / 100.0
"""
def solution(progresses, speeds):
    answer = []
    rest = []
    for p, s in zip(progresses, speeds) :
        if (100-p)%s == 0 :
            rest.append((100-p)//s)
        else :
            rest.append((100-p)//s+1)

    function_c = 1
    value = rest[0]
    for i in range(1, len(rest)) :
        if value >= rest[i] :
            function_c +=1
        else :
            answer.append(function_c)
            function_c = 1
        if i == len(rest)-1 :
            answer.append(function_c)
            break
    return answer



def solution(progresses, speeds):
    rest = []
    for p, s in zip(progresses, speeds) :
        if (100-p)%s == 0 :
            rest.append((100-p)//s)
        else :
            rest.append((100-p)//s+1)

    value = rest[0]
    idx = 1
    d = {rest[0] : 1}
    for idx in range(1, len(rest)) :
        if value < rest[idx] :
            d[rest[idx]] = 1
            value = rest[idx]
        else :
            d[value]+=1

    result = list(d.values())
    return result


# 다른 사람 풀이
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))