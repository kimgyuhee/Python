"""
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 
return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, d, included):
    answer = 0
    for i in range(len(included)) :
        if included[i] :
            answer +=(i*d)+a
    return answer

# 다른 사람 풀이
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer

"""
정수로 이루어진 문자열 n_str이 주어질 때, 
n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.
"""
def solution(n_str):
    for i in range(len(n_str)) :
        if n_str[i] != "0" :
            idx = i
            break
    return n_str[idx:]

# 다른 사람 풀이 1
def solution(n_str):
    return n_str.lstrip('0')


# 다른 사람 풀이 2
def solution(n_str):
    return str(int(n_str))

f = "23455"
print(f[3:])

"""
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. 
queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.

각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 
return 하는 solution 함수를 완성해 주세요.
"""

def solution(arr, queries):
    for i, j in queries :
        arr[i], arr[j] = arr[j], arr[i]
    return arr


"""
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, 
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.
"""
def solution(my_string, s, e):
    answer = my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    return answer

