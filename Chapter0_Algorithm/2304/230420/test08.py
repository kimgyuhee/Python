"""
2016년 1월 1일은 금요일입니다. 
2016년 a월 b일은 무슨 요일일까요? 

두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, 
solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 
화요일이므로 문자열 "TUE"를 반환하세요.
"""
from datetime import datetime
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
def solution(a, b):
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    date = f'2016-{a}-{b}'
    datetime_date = datetime.strptime(date, '%Y-%m-%d')
    value = datetime_date.weekday()
    return days[value]


# 런타임 에러
def solution(a,b):
    answer = ""
    if a>=2:
        b+=31
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30#4월
                    if a>=6:
                        b+=31#5월
                        if a>=7:
                            b+=30#6월
                            if a>=8:
                                b+=31#7월
                                if a>=9:
                                    b+=31#8월
                                    if a>=10:
                                        b+=30#9월
                                        if a>=11:
                                            b+=31#10월
                                            if a==12:
                                                b+=30#11월
    b=(b+3)%7

    print(b)
    return days[b]


# 가장 좋은 코드
def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    dayLen = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 5
    for i in range(0, a - 1) :
        now += dayLen[i]

    answer = (now + b - 1) % 7

    return days[answer]
print(solution(5, 24))