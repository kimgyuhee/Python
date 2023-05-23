"""
문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 
해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 
return하도록 solution 함수를 완성해주세요. "l"이나 "r"이 없다면 빈 리스트를 return합니다.

"""
st = "2345"
print(st.find("1"))
# 합계: 80.0 / 100.0
def solution(str_list):
    str_list = " ".join(str_list)
    index_l = str_list.find("l")
    index_r = str_list.find("r")
    if index_l + index_r == -2 or len(str_list) == 1:
        return []
    else :
        if index_l < index_r:
            return str_list[:index_l].split()
        else :
            return str_list[index_r+1:].split()
        

# 합계: 65.0 / 100.0
# 런타임에러
def solution(str_list):
    answer = []
    for i in range(len(str_list)) :
        if str_list[i] == "l" :
            for j in range(i) :
                answer.append(str_list[j])
            break
        elif str_list[i] == "r" :
            for j in range(len(str_list)-i) :
                answer.append(str_list(i+j+1))
            break
        else :
            continue

    return answer

# 성공 반복문 -> 슬라이싱
def solution(str_list):
    answer = []
    for i in range(len(str_list)) :
        if str_list[i] == "l" :
            answer = str_list[:i]
            break
        elif str_list[i] == "r" :
            answer = str_list[i+1:]
            break
        else :
            continue
    return answer


# 다른 사람 코드 이해
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []
      
print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))