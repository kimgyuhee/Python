"""
문자열 배열 strArr가 주어집니다. 
배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 
제거하고 남은 문자열을 순서를 유지하여 배열로 
return 하는 solution 함수를 완성해 주세요.
"""

def solution(strArr):
    answer = []
    for s in strArr :
        if "ad" not in s :
            answer.append(s)
    return answer

# 다른 사람 풀이 ; 한 줄 코딩
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]

"""
이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.

두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
두 정수 배열 arr1과 arr2가 주어질 때, 
위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, 
arr1이 크다면 1, 
두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(arr1, arr2):
    if len(arr1) > len(arr2) :
        return 1
    elif len(arr1) < len(arr2) :
        return -1
    else :
        if sum(arr1) > sum(arr2) :
            return 1
        elif sum(arr1) < sum(arr2) :
            return -1
        else :
            return 0
        

"""
문자열 myString이 주어집니다. 
"x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 
사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 빈 문자열은 반환할 배열에 넣지 않습니다.
"""

def solution(myString):
    answer = myString.split("x")
    result = []
    for a in answer :
        if a == "" :
            continue
        result.append(a)
    return sorted(result)

# 다른 사람 풀이 ; 한 줄 코딩
def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch)