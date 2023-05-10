"""
정수 배열 arr가 주어집니다. 
arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 
50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때,
arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을 
return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.
"""
dict = {0 : [2,3,4,5,1] ,-1 : [0,0]}
print(dict[0]!=dict[-1])

def solution(arr):
    answer = [[0,0], arr]
    idx = 0
    while answer[idx] != answer[idx+1] :
        a = answer[idx+1]
        result = []
        for i in range(len(a)) :
            if a[i] >= 50 and a[i]%2 == 0 :
                result.append(a[i]//2)
            elif a[i] < 50 and a[i]%2 == 1 :
                result.append(a[i]*2+1)
            else :
                result.append(a[i])

        answer.append(result)
        print(idx, answer)
        idx +=1
    return idx-1

print(solution([1, 2, 3, 100, 99, 98]))

# 다른 사람 풀이 1
def solution(arr):
    answer = 0
    old = arr
    while(True):
        new = []
        for i in old:
            if i>=50 and i%2 == 0:
                i = i/2
            elif i<50 and i%2 == 1:
                i = i*2 + 1
            new.append(int(i))
        if old == new:
            break
        else:
            old = new
            answer += 1
    return answer

# 다른 사람 풀이 2
def solution(arr):
    ret = 0
    while True:
        tmp = list(map(lambda x: x // 2 if x >= 50 and ~x & 1 else x * 2 + 1 if x < 50 and x & 1 else x, arr[:]))
        if arr == tmp:
            break
        arr = tmp[:]
        ret += 1

    return ret