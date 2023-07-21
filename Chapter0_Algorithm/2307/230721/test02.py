""" 
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 
다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법   124나라  10진법   124나라
1	    1	    6	    14
2	    2	    7	    21
3	    4	    8	    22
4	    11	    9	    24
5	    12	    10	    41


자연수 n이 매개변수로 주어질 때, 
n을 124 나라에서 사용하는 숫자로 바꾼 값을 
return 하도록 solution 함수를 완성해 주세요.
"""

def ternary(n) :
    result = ""
    while n :
        n, r = divmod(n, 3)
        result+=str(r)

    return result[::-1]

def ternary1(n) :
    result = ""
    while n :
        n, r = divmod(n, 4)
        result+=str(r)

    return result[::-1]

def solution(n):
    if n == 1 or n == 2:
        return n
    
    answer = ternary(n)
    print(f"{n}을 3진수로 변경한 값 : ",answer)
    answer = answer.replace("2", "4")
    print("2를 4로 변경", answer)
    answer = answer.replace("1", "2")
    print("1을 2로 변경", answer)
    answer = answer.replace("0", "1")
    print("0를 1로 변경", answer)
    return int(answer)


for i in range(1, 11) :
    print(solution(i))


from itertools import product
def solution(n) :
    country124 = []
    count = 1
    while len(country124) < 50000000 :
        print(count)
        result = list(product([1, 2, 4], repeat=count))
        for r in result :
            value = "".join(list(map(str, r)))
            if value == str(n) :
                return value
            country124.append(value)

        count +=1

    tupleN = tuple(list(str(n)))
    print(tupleN)
    print(country124)
    answer = country124.index(tupleN)
    return answer






from itertools import product
def solution(n) :
    country124 = []
    count = 1
    while len(country124) < 5000 :
        result = list(product([1, 2, 4], repeat=count))
        for r in result :
            value = "".join(list(map(str, r)))
            country124.append(value)
        count +=1

    answer = country124[n-1]
    return answer

for i in range(1, 20) :
    print(i, "=>" , solution(i), " | 요상한 나의 식 =>",ternary1(i),ternary(i))