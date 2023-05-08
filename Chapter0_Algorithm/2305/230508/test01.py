"""
정수 배열 date1과 date2가 주어집니다. 
두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 
각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.

만약 date1이 date2보다 앞서는 날짜라면 1을, 
아니면 0을 return 하는 solution 함수를 완성해 주세요.
"""
def compare_num(a, b) :
    if a == b :
        return True, 0
    elif a > b :
        return False, 0
    else :
        return False, 1

def solution(date1, date2):
    answer = 0
    for a, b, in zip(date1, date2) :
        result, n = compare_num(a, b)
        if not result :
            answer = n
            break
    return answer


# 다른 사람 풀이 1
def solution(date1, date2):
    return 1 if int(''.join(str(i) for i in date1)) < int(''.join(str(i) for i in date2)) else 0

"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. q
ueries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr, queries):
    for s, e, k in queries :
        print(s, e, k)
        for i in range(s, e+1) :
            print(arr[i])
            if i%k == 0 :
                arr[i]+=1
            
    return arr

print(solution([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]))