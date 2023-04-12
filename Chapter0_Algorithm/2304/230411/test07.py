"""
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 
return하도록 solution 함수를 완성해주세요.
"""

def solution(score):
    answer = []
    result = {}
    rank = []
    for i, s in enumerate(score) :
        answer.append([0,sum(s)])

    answer.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(answer)-1) :
        if answer[i][1] == answer[i+1][1] :
            answer[i+1][0]-=1
        answer[i][0]+=(i+1)

    answer[len(answer)-1][0] = len(answer)
    for a in answer :
        result[a[1]] = a[0]

    for s in score :
        rank.append(result[sum(s)])

    return rank


def solution(score):
    list_sum = []
    dic_rank = {}
    result = []
    for s in score :
        list_sum.append(sum(s))

    list_sum.sort(reverse=True)

    rank = 1
    for ls in list_sum :
        if ls not in dic_rank :
            dic_rank[ls] = rank
        rank +=1
        
    for s in score :
        result.append(dic_rank[sum(s)])

    return result


# 다른 사람 풀이
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

print(solution([[80, 70], [70, 80]]))
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
print("=====")
dic = {140 : 1, 150 : 2}
print(dic[140])
if 140 in dic :
    print("ㅡ아아아아앙ㄱ")