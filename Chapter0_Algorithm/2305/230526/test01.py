"""
철호는 수열을 가지고 놀기 좋아합니다. 
어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 
원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 
예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.

원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 
연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때, 
원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 
return 하도록 solution 함수를 완성해주세요.
"""

from collections import deque


def solution(elements):
    answer = 0
    result = []
    for i in range(len(elements)) : # 0, 1, 2, 3, 4
        for j in range(len(elements)) : # 0, 1, 2, 3, 4
            value = elements[i:j+1]
            if value == [] :
                continue
            print(">>>", i, j, value)
            for k in range(len(elements)) :
                print(len(value), abs(j-i+1))
                if len(value) == abs(j-i+1) :
                    break
                value.append(elements[k])
            print(value)
            if sum(value) not in result :
                result.append(sum(value))
    print(sorted(result))
    return len(result)


d = deque([1, 2,3])

print(list(d)[0:1])

def solution(elements):
    deque_e = deque(elements)
    result = []
    for i in range(len(elements)) :
        value = list(deque_e)[:i]
        if sum(value) not in result :
            result.append(sum(value))

        e = deque_e.popleft()
        deque_e.append(e)
        print(deque_e)
    return len(sorted(result))

"""
채점 결과
정확성: 10.0
합계: 10.0 / 100.0
> 시간초과
"""
def solution(elements):
    deque_e = deque(elements)
    result = []
    for i in range(len(elements)) :
        for j in range(len(elements)) :
            value = list(deque_e)[:j]
            print(value)
            if sum(value) not in result :
                result.append(sum(value))

        e = deque_e.popleft()
        deque_e.append(e)
        print(deque_e)
    return len(sorted(result))


from collections import deque

def solution(elements):
    deque_e = deque(elements)
    result = []
    for i in range(len(elements)) :
        for j in range(len(elements)) :
            value = list(deque_e)[:j]
            result.append(sum(value))

        e = deque_e.popleft()
        deque_e.append(e)
    
    s = set(result)
    return len(s)

# 다른 사람 풀이 보기
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)



print(solution([7,9,1,1,4]))

v = [7,9,1,1,4]

print(v[2:2])