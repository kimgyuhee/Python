"""
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
정수가 담긴 배열 numlist와 정수 n이 주어질 때 
numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(numlist, n):
    answer = [abs(i-n) for i in numlist]
    l = list(zip(numlist, answer))
    l.sort(key=lambda x : (x[1], -x[0]))
    result = []
    for num in l :
        result.append(num[0])
    return result

# 다른 사람 풀이
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))
