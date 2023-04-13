"""
등차수열 혹은 등비수열 common이 매개변수로 주어질 때,
마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(common):
    def arithmetic(common) :
        formula = True
        answer = 0
        diff = common[1]-common[0]
        for i in range(0, len(common)-1) :
            print(diff, common[i+1]-common[i])
            if common[i+1]-common[i] != diff :
                formula = False
                break
        answer = common[len(common)-1]+diff
        return formula, answer
    
    def geometric(common) :
        formula = True
        answer = 0
        diff = common[1]//common[0]
        for i in range(0, len(common)-1) :
            if common[i+1]//common[i] != diff :
                formula = False
                break
        answer = common[len(common)-1]*diff
        return formula, answer

    artTF, valueA = arithmetic(common)
    geoTF, valueG = geometric(common)
    print(artTF, valueA)
    print(geoTF, valueG)

    if artTF :
        print("등차수열 입니다.")
        return valueA
    elif geoTF :
        print("등비수열 입니다.")
        return valueG
    else :
        print("혹시모를에러")
        return "error"

# 합계: 66.7 / 100.0
# 런타임 에러
def solution(common):
    formula1 = True
    formula2 = True
    if common[0] == 0 :
        diff2 = 0
    else :
        diff1 = common[1]-common[0]
        diff2 = common[1]//common[0]
    for i in range(0, len(common)-1) :
        if common[i+1]-common[i] != diff1 :
            formula1 = False
        if common[i+1]//common[i] != diff2 :
            formula2 = False
    
    value1 = diff1 + common[len(common)-1]
    value2 = diff2 * common[len(common)-1]

    if formula1 :
        return value1
    elif formula2 :
        return value2
    else :
        return "error"
    
# 쳇,,, 인공지능 요놈 아주 똑똑하군,,, 분하다,,,
def solution(common):
    # 등차수열인지, 등비수열인지 판단
    if common[1] - common[0] == common[-1] - common[-2]:  # 등차수열인 경우
        next_num = common[-1] + (common[1] - common[0])
    else:  # 등비수열인 경우
        next_num = common[-1] * (common[1] // common[0])
    return next_num

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))