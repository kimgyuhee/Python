"""

"""
def case1(stroe, n1, n2) :
    find_idx, move_idx = 0,0
    for key, value in stroe.items() :
        if n2 in value :
            find_idx = key
            break

    for key, value in stroe.items() :
        if n1 in value :
            move_idx = key
            break

    value = stroe[find_idx]
    stroe[move_idx]+=value
    stroe[find_idx] = []
    return stroe

def case2(store, n1, n2) :
    find_key = 0
    for key, value in store.items() :
        if n1 in value :
            if n2 in value :
                find_key = key
                break
    
    v = store[find_key]
    print(v)
    min = v.index(n1)
    max = v.index(n2)
    store[find_key] = value[min:max+1]
    store[len(store)] = value[:min]+value[max+1:]
    return store

def case3(store, n1, n2) :
    for key, value in store.items() :
        if n1 in value :
            if n2 in value :
                return "Yes"
    return "No"

def solution(n, queries) :
    answer = []
    save_order = {n : [n] for n in range(n)}
    for q in queries :
        if q[0] == 1 : # 집합 이동
            save_order = case1(save_order, q[1], q[2])
            print(save_order)
        elif q[0] == 2 :  # 새로운 집합 생성
            print("case2 함수 작성중... (이해중...)")
            save_order = case2(save_order, q[1], q[2])
            print(save_order)
        elif q[0] ==  3 : # 같은 집합인지 확인
            result = case3(save_order, q[1], q[2])
            answer.append(result)
        else :
            print("입력이 잘못되었습니다.")

    return answer


print("="*30)
#print(solution(4, [[3,2,3],[1,3,2],[3, 2, 3], [1,2,0], [3,0,1],[2,2,0],[3,2,3],[3,0,2]]))
#print(solution(7, [[1,0,1],[1,2,3],[3,1,3],[1,2,0],[3,1,3],[1,1,5],[1,5,4],[3,4,5],[2,2,5],[3,4,5]]))
"""
d = [[3, 2], [3], [2], [1,2,3], [0, 2, 1]]
for i in d :
    if 3 in i :
        if 2 in i :
            print(f"{i} 존재합니다")
            continue
    print(f"{i} 존재하지 않습니다")
"""

print("="*30)

# 채점 결과
# 정확성: 2.4
# 효율성: 0.0
# 합계: 2.4 / 35.0
def case1(stroe, n1, n2) :
    find_idx, move_idx = 0,0
    for key, value in stroe.items() :
        if n2 in value :
            find_idx = key
            break

    for key, value in stroe.items() :
        if n1 in value :
            move_idx = key
            break

    value = stroe[find_idx]
    stroe[move_idx]+=value
    stroe[find_idx] = []
    return stroe

def case2(store, n1, n2) :
    find_key = 0
    for key, value in store.items() :
        if n1 in value :
            if n2 in value :
                find_key = key
                break
    
    v = store[find_key]
    print(v)
    min = v.index(n1)
    max = v.index(n2)
    store[find_key] = value[min:max+1]
    store[len(store)] = value[:min]+value[max+1:]
    return store

def case3(store, n1, n2) :
    for key, value in store.items() :
        if n1 in value :
            if n2 in value :
                return "Yes"
    return "No"

def solution(n, queries) :
    answer = []
    save_order = {n : [n] for n in range(n)}
    for q in queries :
        if q[0] == 1 : # 집합 이동
            save_order = case1(save_order, q[1], q[2])
            print(save_order)
        elif q[0] == 2 :  # 새로운 집합 생성
            print("case2 함수 작성중... (이해중...)")
            save_order = case2(save_order, q[1], q[2])
            print(save_order)
        elif q[0] ==  3 : # 같은 집합인지 확인
            result = case3(save_order, q[1], q[2])
            answer.append(result)
        else :
            print("입력이 잘못되었습니다.")

    return answer

print(solution(4, [[3,2,3],[1,3,2],[3, 2, 3], [1,2,0], [3,0,1],[2,2,0],[3,2,3],[3,0,2]]))
print(solution(7, [[1,0,1],[1,2,3],[3,1,3],[1,2,0],[3,1,3],[1,1,5],[1,5,4],[3,4,5],[2,2,5],[3,4,5]]))


d = {0:[2,3,1], 1:[2,3], 2 : []}
for key, value in d.items() :
    if [2, 3] in value :
        print("Tes")
    else :
        print("No")