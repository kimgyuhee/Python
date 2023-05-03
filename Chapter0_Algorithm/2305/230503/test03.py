"""
정수 리스트 num_list와 정수 n이 주어질 때, 
num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠
n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 
붙인 리스트를 return하도록 solution 함수를 완성해주세요.
"""

def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    return answer

"""
알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 
알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 
return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString):
    answer = ''
    for s in myString :
        if ord(s) < ord("l") :
            answer +="l"
        else :
            answer +=s
    return answer

# 새롭게 알게 된 함수 translate
# 다른 사람 풀이 1
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

# translate는 문자만 변환 합니다. 
# 예를들어 "Hello, World!"가 있을 경우 H는 숫자 1로, W는 숫자 2로, d는 숫자 3으로 등 지정한 문자를 특정 문자로 변환 시킬 수 있습니다. 
# 아래와 같이 코드를 작성 하면 변환된 "1ello, 2orl3!" 문자열이 출력 됩니다.

print(ord("a"), ord("l"))

# 다른 사람 풀이 2
def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)

"""
모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, 
x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 
언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.

그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.

계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.

임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 
초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.
"""

def solution(n):
    answer = []
    while n!=1 :
        answer.append(n)
        if n % 2 == 0 :
            n = n //2
        else :
            n = 3 * n + 1
    return answer +[1]

"""
정수 배열 arr과 delete_list가 있습니다. 
arr의 원소 중 delete_list의 원소를 모두 삭제하고 
남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 
return 하는 solution 함수를 작성해 주세요.
"""

def solution(arr, delete_list):
    answer = []
    for a in arr :
        if a not in delete_list :
            answer.append(a)
    return answer