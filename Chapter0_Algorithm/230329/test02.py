"""
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
"""

# 문자열에 공백이 연속으로 여러개 나왔을 떄 split 했을 경우 결과
s = "2222     3 4 5 1  f as d  f d     asdf"
s = s.split(" ")
print(s)

def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
print(Jaden_Case("3people    unFollowed me for the last week hi       hello"))

print("#################")
def Jaden_Case1(s) :
    answer = ""
    s = s.lower()
    for i in s.split() :
        if len(i) == 0:
            answer += ""
        elif i[0].isdigit() :
            answer += i
        else :
            i = i.replace(i[0], i[0].upper())
            answer += (i+" ")

    #print(answer[0 : -1])
    return answer[0 : -1]

print(Jaden_Case1("3people unFollowed me for the last week"))
print(Jaden_Case1("3people    unFollowed me for the last week hi       hello"))