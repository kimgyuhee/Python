"""
정수 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(array, n):
    def compareAB(a, b, n) :
        if abs(a-n) > abs(b-n) :
            return b
        else :
            return a
        
    array.append(n)
    array.sort()
    print(array)

    index = array.index(n)
    if index == 0 :
        return array[index+1]
    elif index == len(array)-1 :
        return array[index-1]
    else :
        print("비교할겁니다 :)")
        a = array[index-1]
        b = array[index+1]
        print(a, b)
        result = compareAB(a, b, n)
        return result


# 다른 사람 풀이
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer


print(solution([3, 10, 28] , 20))
print(solution([10, 11, 12], 13))