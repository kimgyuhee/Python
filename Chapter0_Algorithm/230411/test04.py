"""
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 
서비스 치킨에도 쿠폰이 발급됩니다. 
시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 
최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.


"""

def solution(chicken):
    sum = answer
    answer = chicken//10
    for i in range(1, len(str(chicken))-1) :
        print(i, answer)
        sum +=(answer//10)
    return answer


def solution(chicken):
    coupon = []
    service = chicken//10
    sum = service
    rest = chicken%10
    coupon.append(rest)
    service += rest
    for i in range(1, len(str(chicken))-1) :
       # print(service)
       rest = service%10
       service = service//10
       sum+=service
       coupon.append(rest)
       service += rest
       # print(service, rest, sum, coupon)

    print(coupon)
    return sum

# 다른 사람 풀이
def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        eaten = coupon // 10
        answer += eaten
        coupon = coupon % 10 + eaten
    
    return answer

print(solution(100))
print("==========")
print(solution(1081))

print(8//10)
