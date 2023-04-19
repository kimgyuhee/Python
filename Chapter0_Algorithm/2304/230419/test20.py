"""
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 
n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

"""

def solution(strings, n):
    answer = sorted(strings, key=lambda x : x[n])
    return answer


def solution(strings, n):
    result = []
    answer = [[str[n], str] for str in strings]
    a = sorted(answer, key=lambda x : (x[0], x[1]))
    for value in a :
        result.append(value[1])
    return result



print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))