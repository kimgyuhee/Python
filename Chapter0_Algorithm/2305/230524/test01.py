"""
0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다. 
등수가 높은 3명을 선발해야 하지만, 
개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 
전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다. 
전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 
각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c
를 return 하는 solution 함수를 작성해 주세요.
"""


def solution(rank, attendance):
    answer = []
    n = 0
    for r, a in zip(rank, attendance) :
        if a :
            answer.append([r, n])
        n+=1
    
    answer.sort()

    result = answer[0][1]*10000+answer[1][1]*100+answer[2][1]
    return result

# 다른사람 풀이
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]	))