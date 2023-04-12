def solution(n, m, x, y, z):

    answer = { i : 0 for i in range(1, n+1) }
    number = { i : 0 for i in range(1, n+1) }
    allNummber = list(zip(x, y, z))
    print(allNummber)
    print(answer)

    nowIndex = 0
    for a in allNummber :
        # print(a)
        number[a[0]] += 1
        number[a[1]] += 1
               
        answer[a[0]] +=a[2]
        answer[a[1]] +=a[2]

    print(answer)
    print(number)
    return answer

print(solution(3, 3, [1,1,2], [3,2,3], [1,5,2]))

"""
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.
예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때,
거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

"""

def solution1(triangle):
    answer = 0
    
    idx = 2
    for i in range(1, len(triangle)):
        for j in range(idx):
            print("#"*30)
            print(f"i : {i} \nj : {j} \n=====> idx : {idx}")
            print(f"triangle > ==== {triangle[i][j]}")
            print(triangle)
            print("#"*30)
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            print("="*15)
            print(triangle)
            print("="*15)
        idx += 1
    answer = max(triangle[-1])
    return answer

a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution1(a))


print("\n\n\n\n")
a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(a[0][0])
print(a[1][0])
print(a[1][1])
print(a[2][1])
print(a[4][1])

a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print()
idx = 2
for i in range(1, 5):
    for j in range(idx):
        print(i, j)

