"""
정수 num과 k가 매개변수로 주어질 때, 
num을 이루는 숫자 중에 k가 있으면 
num의 그 숫자가 있는 자리 수를 return하고 
없으면 -1을 return 하도록 solution 함수를 완성해보세요.
"""
# TypeError: must be str, not int
# 당황스러운 에러 발생...?
"""
해결 !!!
answer = numStr.find(str(k))
numStr : str    |   k : int
형이 같지 않아서 생긴 에러이다.
k를 str로 변환해줬더니 해결 완료😉 
"""
def solution(num, k):
    answer = -1
    numStr = str(num)
    answer = numStr.find(str(k))
    if answer == -1 :
        return -1
    else : 
        return answer + 1


# 다른 사람 풀이
def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))
