"""
정수 리스트 num_list가 주어질 때, 
마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 
마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    if num_list[-1] > num_list[-2] :
        num_list.append(num_list[-1]-num_list[-2])
    else :
        num_list.append(num_list[-1]*2)
    return num_list


"""
정수 리스트 num_list와 정수 n이 주어질 때, 
num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 
return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n) :
        answer.append(num_list[i])
    return answer

# 다른 사람 풀이
def solution(num_list, n):
    return num_list[::n]

"""
정수가 담긴 리스트 num_list가 주어집니다. 
num_list의 홀수만 순서대로 이어 붙인 수와
짝수만 순서대로 이어 붙인 수의 합을 
return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list):
    even = ""
    odd = ""

    for num in num_list :
        if num%2==0 :
            even +=str(num)
        else :
            odd +=str(num)

    return int(even)+int(odd)

# 다른 사람 풀이
def solution(num_list):
    even=int(''.join([str(i) for i in num_list if i%2==0]))
    odd=int(''.join([str(i) for i in num_list if not i%2==0]))
    return even+odd
# 시간 복잡도 두배

"""
문자열 배열 strArr가 주어집니다. 
모든 원소가 알파벳으로만 이루어져 있을 때, 
배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 
짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.
"""

def solution(strArr):
    answer = []
    num = 0
    for s in strArr :
        if num%2==0 :
            answer.append(s.lower())
        else :
            answer.append(s.upper())
        num+=1
    return answer
