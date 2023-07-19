"""
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 
길이 5 이하의 모든 단어가 수록되어 있습니다. 
사전에서 첫 번째 단어는 "A"이고, 
그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 
이 단어가 사전에서 몇 번째 단어인지 
return 하도록 solution 함수를 완성해주세요.
"""


from itertools import combinations, permutations
from itertools import combinations_with_replacement
# from itertools import product
alpha = ['A', 'E', 'I', 'O', 'U']
def solution(word):
    answer = 0
    dictionary = []

    for i in range(5) :
        perm = list(combinations_with_replacement(alpha, i+1))
        for p in perm :
            value = "".join(p)
            dictionary.append(value)

    dictionary.sort()
    print(dictionary.index('O'))
    return dictionary.index(word) + 1


from itertools import product
alpha = ['A', 'E', 'I', 'O', 'U']
def solution(word):
    dictionary = []

    for i in range(5) :
        data = product(alpha, repeat=i+1)
        for d in data :
            value = "".join(d)
            dictionary.append(value)

    dictionary.sort()
    print(dictionary.index('O'))
    return dictionary.index(word) + 1


print(solution("AAAAE"))