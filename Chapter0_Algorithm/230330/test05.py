"""
재귀함수
* 종료 조건 포함 *

DFS(깊이 우선 탐색) Depth-First Search
깊은 부분을 우선적으로 탐색하는 알고리즘
DFS는 스택 자료구조(혹은 재귀함수)를 이용
1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 합니다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라고 있으면 그 노드를 스택에 넣고
방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다
3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복합니다.
"""

from collections import deque


def recursive_f(i) :
    if i == 10 :
        return
    
    print(f"param -> i : {i} 에서 i+1 : {i+1} 함수를 호출")
    recursive_f(i+1)
    print(f"{i}번째 함수를 종료")

recursive_f(1)


result = []
def fac(n) :
    global result
    if n <= 1 :
        result.append(n)
        return 1
    result.append(n)
    print(result)
    return n * fac(n-1)

n = fac(5)
s = " * ".join(list(map(str, result)))
print()
print(f"팩토리얼 결과 : {s} = {n}")

result = []
n = fac(1)
s = " * ".join(list(map(str, result)))
print()
print(f"팩토리얼 결과 : {s} = {n}")

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [[],[2,3,4],[1,7],[1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * len(graph) #(index 0은 사용하지 않기 위함)

dfs(graph, 1, visited)
print()
print("="*30)
print()
def bfs(graph, start, visited) :
    queue = deque([start])
    print(queue)
    visited[start] = True 
    while queue :
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


graph = [[],[2,3,4],[1,7],[1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * len(graph) #(index 0은 사용하지 않기 위함)
bfs(graph, 1, visited)
print()

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start_node):
 
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    ## 시작 노드를 시정하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited


need_visited, visited = list(), list()
print(need_visited)
print(visited)

need_visited.extend(graph["A"])
print(need_visited)

print(dfs(graph, "A"))

print("""
스택/큐를 구현할 때는 collection라는 패키지에서 deque를
활용하시는 것을 추천드립니다.
논리는 저의 동일합니다만, 
성능면에서 list() 형태보다 deque 형태가 훨씬 좋아요!
""")

def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    
    ##시작 노드 설정해주기
    need_visited.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
                
    return visited


def dfs_recursive(graph, start, visited = []):
## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

print(dfs_recursive(graph,"A"))


def bfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.popleft()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited

print(bfs(graph,"A"))
print(bfs(graph,"J"))