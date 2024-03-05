import sys
from collections import deque

# 입력 받기
n, k = map(int, input().split())

# 양방향 연결 리스트(deque) 생성
deq = deque([i for i in range(1, n+1)])

# 요세푸스 순열 생성
res = []
while len(deq) != 0:
    for _ in range(k-1):
        # k-1번째 노드까지 deq 맨 뒤로 이동
        deq.append(deq.popleft())
    # k번째 노드 삭제 후 결과 배열에 추가
    res.append(str(deq.popleft()))

# 결과 출력
print('<'+', '.join(res)+'>')


# 입력 받기
n, k = map(int, sys.stdin.readline().split())

# 요세푸스 순열 생성
idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    idx += k - 1  # k-1번째 인덱스까지 건너뛰기
    if idx >= len(queue):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(queue)  # 나머지 연산을 통해 인덱스 계산
    res.append(str(queue.pop(idx)))  # k번째 수 제거 후 결과 배열에 추가

# 결과 출력
print("<", ", ".join(res), ">", sep="")

