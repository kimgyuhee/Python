"""
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
정수 배열 array가 매개변수로 주어질 때,
최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

"""

def solution(array):
    result = {}
    for a in array :
        if a not in result :
            result[a] = 1
        else :
            result[a] +=1
        
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    if len(array) == 1 :
        return result[0][0]
    else :
        # print(result)
        # print(result[0][0], result[1][0])
        if result[0][1] == result[1][1] :
            return -1
        else :
            return result[0][0]


def solution(array):
    result = {}
    for a in array :
        if a not in result :
            result[a] = 1
        else :
            result[a] +=1
        
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print(result)
    max = result[0][1]
    print(max)


def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            print(i, a)
            print(array)
            array.remove(a)
        if i == 0: return a
    return -1

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))