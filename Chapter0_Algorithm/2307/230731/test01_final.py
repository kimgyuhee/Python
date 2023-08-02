from collections import deque

def solution(x, y, n):
    queue = deque([(y, 0)])
    while queue:
        y, count = queue.popleft()

        if x == y:
            return count
        if x > y:
            continue
        count += 1
        if y % 2 == 0:
            queue.append([y // 2, count])
        if x * 3 <= y:
            queue.append([y // 3, count])
        queue.append([y - n, count])

    return -1



def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        answer+=1

    return -1