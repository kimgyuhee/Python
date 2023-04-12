"""
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
"""

def solution(lines):
    table = [set([]) for _ in range(200)] # -100~100까지 각 선분들의 등장 count 초기화
    print(f"table 변경 전 -> {table}")
    for index, line in enumerate(lines):
        print(f"index -> {index}, line = {line}")
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index) # 선분에 음수가 들어있을 수도 있으므로 +100

    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1
    print(f"table 변경 후 -> {table}")
    return answer


def solution1(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    print(sets)
    print(sets[0] & sets[1])
    print(sets[0] & sets[2])
    print(sets[1] & sets[2])
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


print("========")
print(solution([[0, 5], [3, 9], [1, 10]]))
print("========")
print(solution([[0, 1], [2, 5], [3, 9]]))
print("========")
print(solution([[-1, 1], [1, 3], [3, 9]]))
print("========")



print("========")
print(solution1([[0, 5], [3, 9], [1, 10]]))
print("========")
print(solution1([[0, 1], [2, 5], [3, 9]]))
print("========")
print(solution1([[-1, 1], [1, 3], [3, 9]]))
print("========")

a = set([2,3,4,5,1,6])
b = set([1,2,3])
print(a-b)