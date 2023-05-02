"""
문자열들이 담긴 리스트가 주어졌을 때, 
모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 
꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다. 
예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 
문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.

문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, 
str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 
return하도록 solution 함수를 완성해주세요.

"""
def solution(str_list, ex):
    answer = ''
    for str in str_list :
        if ex not in str :
            answer +=str
    return answer

"""
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, 
is_suffix가 my_string의 접미사라면 1을, 
아니면 0을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, is_prefix):
    return int(my_string.endswith(is_prefix))


def solution(my_string, is_prefix):
    answer = []
    for i in range(0, len(my_string)) :
        answer.append(my_string[i:])
    print(answer)
    if is_prefix in answer :
        return 1
    else :
        return 0
    
"""
정수 리스트 num_list가 주어집니다. 
가장 첫 번째 원소를 1번 원소라고 할 때, 
홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.
"""

def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for num in num_list :
        if answer%2== 0 :
            odd+=num
        else :
            even+=num
        answer+=1

    return max(odd, even)