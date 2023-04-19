"""
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, 
solution을 완성하세요. 

예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

"""

def solution(n):
    answer = ''
    for i in range(n) :
        if i%2 == 0 :
            answer +="수"
        else :
            answer +="박"
    return answer

def solution(n):
    str = "수박"*n
    return str[:n]

print(solution(3))
print(solution(4))

print("수박수")

