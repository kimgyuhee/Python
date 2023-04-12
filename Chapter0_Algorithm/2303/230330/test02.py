"""
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0]
비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

"""

def queueDef (op) :
    answer = []

    for o in op :
        answer.sort()
        command, n = o.split(" ")
        if command == "I" :
            answer.append(int(n))
        elif command == "D" :
            if len(answer) == 0 :
                continue
            if n == "1" :
                answer.pop()
            elif n == "-1" :
                answer.reverse()
                answer.pop()

    result = []
    if len(answer) == 0 :
        result = [0,0]
    else :
        result = [max(answer), min(answer)]
    return result



print(queueDef(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(queueDef([]))
print(queueDef(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(queueDef(["I 3"]))