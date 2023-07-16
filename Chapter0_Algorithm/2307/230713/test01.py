"""
예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 
2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 
다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 
이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 
"abcabc2de"가 되지만, 3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 
이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 
위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 
return 하도록 solution 함수를 완성해주세요.
"""


from collections import deque
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1) :
        result = deque([])
        for j in range(0,len(s), i) :
            result.append(s[j:j+i])
        print(i, result)
        str_len = 1
        str_zip = ""
        value = result.popleft()
        for i in range(len(result)):
            v = result.popleft()
            print(value , v)
            if value == v :
                print(f"{value}와 {v}가 같습니다. ! {str_len}이 1 증가합니다.")
                str_len +=1
                value = v
                if len(result) == 0 :
                    str_zip += str(str_len)+v
                # result.append(str(str_len)+v)
                
            else :
                print("뭐가 문제니", str_len)
                if str_len == 1 :
                    str_zip = str_zip + value
                else :
                    str_zip = str_zip + str(str_len) + value
                    
                if len(result) == 0 :
                    str_zip += v
                value = v
                str_len = 1
            print(len(result))
            print(str_zip)
        
        if len(str_zip) < answer :
            answer = len(str_zip)
        print(str_zip)

    return answer


# 다른 사람 풀이 
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))

    