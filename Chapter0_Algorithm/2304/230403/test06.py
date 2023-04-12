"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

"""

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(1, max(citations)) :
        # print(citations)
        result1 = [1 for c in citations if c >= i ]
        result2 = [1 for c in citations if c > i ]
        # print(result)
        if len(result1) == i or len(result2) == i :
            answer = i
            break
        # else :
        #     answer = sum(result1)
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([3]))
print(solution([0]))
print(solution([3, 0 , 1, 1 ,1 , 6, 1, 5]))
print(solution([3,3,6, 0 , 1, 1 ,1 , 6, 1, 5]))
print(solution([25, 8, 5, 3, 3]))


def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    print(enumerate(citations, start=1))
    print(list(map(min, enumerate(citations, start=1))))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([25, 8, 5, 3, 3]))