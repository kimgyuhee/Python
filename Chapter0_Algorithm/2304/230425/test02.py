"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""

# 정확성: 41.7
# 효율성: 33.3
# 합계: 75.0 / 100.0
# 런타임에러
def solution(participant, completion):
    set1 = set(participant)
    set2 = set(completion)
    answer = set1 - set2
    return answer.pop()

def solution(participant, completion):
    answer = ""
    for p in participant :
        if p not in completion :
            answer = p
            break
    return answer

def solution(participant, completion):
    answer = ""
    for p in participant :
        if p not in completion :
            answer = p
            break
    return answer

from collections import Counter

def solution(participant, completion):
    answer = ''
    p_dict = Counter(participant)
    c_dict = Counter(completion)

    for p_name in p_dict:
        if p_dict[p_name] != c_dict[p_name]:
            answer = p_name

    return answer

# 다른 사람 풀이1
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))