# 채점 결과
# 정확성: 86.7
# 합계: 86.7 / 100.0
# 4, 5, 7, 10  테스트 케이스 오답
import heapq
from itertools import combinations, permutations

def solution(expression):
    numbers = []
    operations = []
    number = ""
    cal = []
    heapq.heapify(cal)

    for e in expression :
        if e.isdigit() :
            number +=e
        else :
            operations.append(e)
            numbers.append(number)
            number = ""
    
    numbers.append(number)

    remove_duplicates_operations = list(set(operations))
    priority_operations = list(permutations(remove_duplicates_operations, len(remove_duplicates_operations)))

    for po in priority_operations :
        cal_op = operations.copy()
        cal_num = numbers.copy()
        for o in po :
            while True :
                if o not in cal_op :
                    break
                else :
                    idx = cal_op.index(o)
                    v1 = cal_num[idx]
                    v2 = cal_num[idx+1]
                    value = eval(v1+o+v2)
                    cal_num.remove(v1)
                    cal_num.remove(v2)
                    cal_op.remove(o)
                    cal_num.insert(idx, str(value))

        if int(cal_num[0]) > 0 :
            heapq.heappush(cal, int(cal_num[0]) * -1)
        else :
            heapq.heappush(cal, int(cal_num[0]))
    
    return abs(heapq.heappop(cal))




# 채점 결과
# 정확성: 100
# 합계: 100 / 100.0
# remove -> del 로 인덱스로 삭제 해줌
import heapq
from itertools import combinations, permutations

def solution(expression):
    numbers = []
    operations = []
    number = ""
    cal = []
    heapq.heapify(cal)

    for e in expression :
        if e.isdigit() :
            number +=e
        else :
            operations.append(e)
            numbers.append(number)
            number = ""
    
    numbers.append(number)

    remove_duplicates_operations = list(set(operations))
    priority_operations = list(permutations(remove_duplicates_operations, len(remove_duplicates_operations)))

    for po in priority_operations :
        cal_op = operations.copy()
        cal_num = numbers.copy()
        for o in po :
            while True :
                if o not in cal_op :
                    break
                else :
                    idx = cal_op.index(o)
                    v1 = cal_num[idx]
                    v2 = cal_num[idx+1]
                    value = eval(v1+o+v2)
                    # cal_num.remove(v1)
                    # cal_num.remove(v2)
                    # cal_op.remove(o)
                    del cal_num[idx]
                    del cal_num[idx]
                    del cal_op[idx]
                    cal_num.insert(idx, str(value))

        if int(cal_num[0]) > 0 :
            heapq.heappush(cal, int(cal_num[0]) * -1)
        else :
            heapq.heappush(cal, int(cal_num[0]))
    
    return abs(heapq.heappop(cal))


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("50*0-3*2"))
