"""
문자열 my_string이 매개변수로 주어집니다. 
my_string에서 중복된 문자를 제거하고
하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_string):
    answer = ''
    for m in my_string:
        if m not in answer :
            answer+=m
    return answer

print(solution("people"))
print(solution("We are the world"))

"""
머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 
문자열 letter가 매개변수로 주어질 때, 
letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
모스부호는 다음과 같습니다.
"""

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    # return ''.join([morse[i] for i in letter.split(' ')])
    
    answer = ''
    l = letter.split(" ")
    for i in l :
        answer +=morse[i]
    return answer

print(solution(".... . .-.. .-.. ---"))