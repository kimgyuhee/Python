"""
사용자의 검색 키워드 기록을 바탕으로 검색어를 추천하는 프로그램을 개발한다.
프로그램은 사용자가 이전에 검색했던 키워드를 저장하고 있으며, 검색 옵션에 따라서 제시되는 키워드가 달라진다.

잡다 - 튜토리얼 - BASE 정답
"""

def solution(history, option, keyword):
    answer = []
    if len(option[0]) == 2:
        for h in history :
            if option[0][1] == "T" :
                check = h.split(" ")
                if keyword in check :
                    answer.append(h)
            else :
                if keyword in h :
                    answer.append(h)


    else : # F인경우
        for h in history :
            if keyword in h :
                answer.append(h)
    return answer


print(solution(["hello i am david",
"hello kail",
"hi tina"], [["W", "T"]], "hello"))

print(solution(["hello i am david",
"hello kail",
"hi tina"], [["W", "T"]], "he"))

print(solution(["hello i am david",
"hello kail",
"hi tina"], [["W"]], "he"))

print(solution(["hello i am david",
"hello kail",
"hi tina"], [["W" , "F"]], "he"))