def solution(msg):
    d = {}
    answer = []
    
    for i in range(26) :
        d[chr(i+65)] = i+1
        
    for i in range(len(msg)) :
        value = msg[i]
        print("i", i)
        print(value)
        for j in range(i, len(msg)-1) :
            print("j 들어왔습니다.",i, j)
            add = msg[j+1]
            if value + add not in d :
                d[value+add] = len(d)+1
                break
            else :
                value = value + add
                
        print(value)
        print("="*20)
        print(d)
        answer.append(d[value])
        print(answer)
        
        
    return answer


from collections import deque
def solution(msg):
    d = {}
    answer = []
    
    for i in range(26) :
        d[chr(i+65)] = i+1
        
    str_deque = deque(list(msg))
    print(str_deque)

    for i in range(len(msg)) :
        value = str_deque.popleft()
        print(str_deque)
        print("i", i)
        print(value)
        for j in range(i, len(msg)-1) :
            print("j 들어왔습니다.",i, j)
            if len(str_deque) == 0 :
                break
            add = str_deque.popleft()
            print(add)
            if value + add not in d :
                d[value+add] = len(d)+1
                str_deque.appendleft(add)
                break
            else :
                value = value + add

        print("변경후의")        
        print(str_deque)
        print(value)
        print("="*20)
        print(d)
        answer.append(d[value])
        print(answer)
        if len(str_deque) == 0 :
            break
        
    return answer


# 다른 사람 풀이 
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer

print(solution("KAKAO"))
print(solution("ABABABABABABABAB"))