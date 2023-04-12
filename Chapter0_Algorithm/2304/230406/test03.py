"""
약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
자연수 n이 매개변수로 주어질 때 
n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

"""

def solution(n):
    # 약수 구하는 함수
    def divisor(n) :
        count = 0
        for i in range(1,n+1) :
            if n%i == 0 :
                count +=1
        return count

    answer = 0 # 정답을 담을 함수
    
    for i in range(1, n+1) :
        if divisor(i) >= 3 :
            answer +=1

    return answer


# 다른 사람 풀이

def get_divisors(n):
    l = list(filter(lambda v: n % v ==0, range(1, n+1)))
    print(l)
    return l

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))


print(solution(1))
print(solution(10))
print(solution(15))

# print(solution())