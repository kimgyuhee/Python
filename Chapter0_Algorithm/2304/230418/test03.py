"""
어떤 정수들이 있습니다.
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 
담은 불리언 배열 signs가 매개변수로 주어집니다. 
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
"""


def solution(absolutes, signs):
    answer = 0
    for a, b in zip(absolutes, signs) :
        if b :
            answer +=a
        else :
            answer -=a

    return answer

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

print(solution([4,7,12], [True,False,True]))