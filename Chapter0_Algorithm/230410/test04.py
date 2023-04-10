"""
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 
7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array):
    answer = 0
    for a in array :
        count = str(a).count("7")
        answer +=count
    return answer

# 다른 사람 풀이
def solution(array):
    return str(array).count('7')


print(solution([7, 77, 17]))
print(solution([10, 29]))

l = [45, 1, 2, 5, 6]
print(str(l))
print(str(l).count('5'))