"""
두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
"""

str1, str2 = input().strip().split(' ')
print(str1+str2)

"""
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, 
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, alp):
    answer = my_string.replace(alp, alp.upper())
    return answer


"""
정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 
return 하는 solution 함수를 작성해 주세요.
"""

def solution(arr, n):
    answer = []
    if len(arr)%2 == 0 :
        for i in range(len(arr)) :
            if i%2 == 1 :
                answer.append(arr[i]+n)
            else :
                answer.append(arr[i])
    else :
        for i in range(len(arr)) :
            if i%2 == 0 :
                answer.append(arr[i]+n)
            else :
                answer.append(arr[i])
    return answer

# 다른 사람 풀이1
def solution(arr, n):
    return [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))] if len(arr) % 2 != 0 else [arr[i] + n if i % 2 != 0 else arr[i] for i in range(len(arr))]

# 다른 사람 풀이2
def solution(arr, n):
    ans = []
    k = len(arr)%2
    for i, a in enumerate(arr):
        if (i+k)%2 != 0:
            ans.append(a+n)
        else:
            ans.append(a)
    return ans

"""
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 
저장한 배열을 return 하는 solution 함수를 완성해 주세요.
"""
def solution(n, k):
    answer = []
    for i in range(n//k) :
        answer.append((i+1)*k)
    return answer

# 다른 사람 풀이1
def solution(n, k):
    return [i for i in range(k,n+1,k)]