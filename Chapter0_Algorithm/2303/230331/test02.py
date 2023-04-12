# DFS 이해 못하겠어요ㅠㅠㅠㅠㅠ
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        print(f"""dfs함수 들어왔어요^^
        computers : {computers}
        visited : {visited}
        start : {start}\n""")
        stack = [start]
        while stack:
            print("stack : ", stack)
            print("visited : ", visited)
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                print("="*15)
                print(f"i : {i}     j : {j}")
                print("conputer : ", computers)
                print("visited : ", visited)
                print("="*15)
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    print(">>> stack : ", stack)
    i=0
    while 0 in visited:
        print("answer >>>>>>>> ",answer)
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
            print("answer : ",answer)
        i+=1
    return answer

print()
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print()
print()
print(solution(3, [[1, 1, 0], [1, 1, 0], [1, 1, 1]]))
print()
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print()
print(solution(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0,0,0,0]]))
print()

print()
print(solution(4, [[0, 1,1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0,0,1,1]]))
print()

print("#####"*10)
checkNum = [0 for _ in range(3)]
print(checkNum)
computers = [[1,1,0], [1,1,0], [0,0,1]]

print(computers[1][2])

computers[1][2] = 1
print(computers)

