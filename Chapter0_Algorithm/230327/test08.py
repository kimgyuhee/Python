from datetime import date
def solution(today, terms, privacies):
    answer = []
    mon = {}
    today_time = date(int(today[:4]), int(today[5:7]),int(today[8:10]))
    print(date.day)
    print()
    print(today_time)
    for sep in terms:
        ter, mont = sep.split(' ') # term의 값들을 띄어쓰기로 분리 후 ter, mont 에 저장
        mon[ter] = mont # 딕셔너리에 키, 값으로 저장
    
    for j,i in enumerate(privacies,1):
        dateday, term = i.split(' ')
        print(dateday)
        year = int(dateday[:4])

        month = int(dateday[5:7]) + int(mon[term])  # 수집된 정보의 달 + 해당 유효기간
        monthPer = int(month / 12) # 전체 달이 12이므로 12로 나눈 몫을 구하여 년도에 더해줌
        year = year + monthPer 
        if int(dateday[8:10]) == 1: # 수집된 정보의 일이 01이라면
            if month % 12 == 0: 
                month = month % 12 -1 
                year -=1
            else:
                month = month % 12 -1
        else:
            month = month % 12

        if month == 0:
            month = 12
            year -=1
        elif month < 0:
            month = 12 + month

        day = dateday[8:10]
        if  day == '01': 
            day = 28
            
        else:
            day = int(day) - 1
        
        old_time = date(year,month,day)
        if today_time > old_time:
            answer.append(j)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))