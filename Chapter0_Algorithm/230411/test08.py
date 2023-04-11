"""
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 
3x 마을 사람들의 숫자는 다음과 같습니다.

정수 n이 매개변수로 주어질 때, 
n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
"""

def solution(n):
    result = {}
    answer = 1
    for i in range(1, n+1) :
        print(i, answer)
        if i%3 == 0 :
            answer +=1
            result[i] = answer
        else :
            if answer%3 == 0 :
                answer +=1
                result[i] = answer
                continue
        result[i] = answer  
        answer +=1
    return result

def solution(n):
    answer = 1
    for i in range(1,n+1) :
        if i%3 == 0 or '3' in str(i):
            answer +=1
        if answer%3 == 0 or '3' in str(answer) :
            answer +=1
        print(f"3X : {answer} / 10진수 : {i}")
        answer +=1
    return answer

def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
    return answer

def solution(n):
    answer = [0, 1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29, 40, 41, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 74, 76, 77, 79, 80, 82, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 101, 104, 106, 107, 109, 110, 112, 115, 116, 118, 119, 121, 122, 124, 125, 127, 128, 140, 142, 145, 146, 148, 149, 151, 152, 154, 155, 157, 158, 160, 161, 164, 166, 167, 169, 170, 172, 175, 176, 178, 179, 181, 182, 184, 185]
    return answer[n]

print(solution(15))
print(solution(40))