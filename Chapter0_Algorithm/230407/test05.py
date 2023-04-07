"""
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
정수 배열 emergency가 매개변수로 주어질 때 
응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

"""

def solution(emergency):
    result = {e : 0 for e in emergency}
    answer = {e : 0 for e in emergency}
    answer = sorted(answer.items(), reverse=True)
    em = []

    for a in range(0, len(answer)) :
        result[answer[a][0]] =a+1

    for e in emergency :
        em.append(result[e])

    return em

# 다른 사람 풀이
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]


print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))



l = [{'Name': 'Alice', 'Age': 40, 'Point': 80}, 
     {'Name': 'Bob', 'Age': 20},
     {'Name': 'Charlie', 'Age': 30, 'Point': 70}]

l.sort(key=lambda x: x['Age'])
