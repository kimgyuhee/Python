"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
"""

def solution(n):
    result = ""
    answer = list(map(int, str(n)))
    answer.sort(reverse=True)
    for a in answer :
        result+=str(a)

    return int(result)

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

print(solution(118372))


print("{0:=^20}".format("다음 문제"))

"""
정수 n이 매개변수로 주어질 때, 
n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(n):
    answer = []
    if n == 1 :
        return [1]
    for i in range(1, n//2) :
        if n%i == 0 :
            answer.append(i)
            answer.append(n//i)
    answer = set(answer)
    result = list(answer)
    result.sort()
    return result


print(solution(1))
print(solution(24))
print(solution(29))
print(solution(10000))