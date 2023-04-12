"""
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(bin1, bin2):
    # answer = ''
    b1 = int(bin1, 2)
    b2 = int(bin2, 2)
    sum = b1+b2
    # print(sum)

    return bin(sum)[2:]

def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer


print(solution("10", "11"))
print(solution("1001", "1111"))