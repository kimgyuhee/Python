"""
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 
18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 

자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

"""
# CASE 문제 이해를 잘 못했어요
def solution(x):
    x = list(map(int, str(x)))
    print(sum(x), len(x))
    if sum(x)%len(x) == 0 :
        return True
    else :
        return False

def solution(x):
    listX = list(map(int, str(x)))
    if x%sum(listX) == 0 :
        return True
    else :
        return False
    
print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))