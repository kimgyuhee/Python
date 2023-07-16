"""
땅따먹기 게임을 하려고 합니다. 
땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 
모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 
각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 
단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |

로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.
마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 
return하는 solution 함수를 완성해 주세요. 

위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 
3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.
"""

def solution(land):
    answer = 0

    for i in range(4) :
        value = 0
        now_idx = i
        value +=land[0][now_idx]
        for j in range(1, len(land)) :
            if land[j].index(max(land[j])) != now_idx :
                now_idx = land[j].index(max(land[j]))
                value +=max(land[j])
            else :
                second_max = land[j].copy()
                second_max.sort()
                now_idx = land[j].index(second_max[-2])
                value +=second_max[-2]

        if answer < value :
            answer = value    

    return answer


def solution(land):
    answer = 0
    n = len(land)

    for i in range(1, n):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
        print(f"{i}번째 반복문")
        print(land)

    answer = max(land[n-1])

    return answer

print("="*20)
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print("="*20)
print(solution([[1, 1, 3, 1], [2, 3, 2, 2], [1, 4, 1, 1]]))
print("="*20)
#print(solution([[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1]]))
#print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
# print(solution())