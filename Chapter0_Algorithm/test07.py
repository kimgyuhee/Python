
def solution(today, terms, privacies):
    def compare(today, date) :
        result = True
        if int(today[0]) > int(date[0]) :
            result = False
        else :
            if (int(today[1]) > int(date[1])) :
                result = False
            else :
                if (int(today[2]) > int(date[2])) :
                    result = False
                

        return result 
    
    answer = []
    today = today.split(".")
    print(today)
    dict = {}
    for t in terms :
        value1, month = t.split(" ")
        dict[value1] = month
        
    print(dict)
    index = 0
    for p in privacies :
        index = index +1
        d, value2 = p.split(" ")
        date = d.split(".")
        print("\n\n")
        print(date)
        
        if int(date[1]) + int(dict[value2]) > 12 :
            date[0] = int(date[0]) + 1
        date[1] = (int(date[1])+int(dict[value2])/12)
        print(f"\ndate 유효기간 {value2} -> ",date)
        print(index)
        if compare(today, date) :
            answer.append(index)
        
        
    
    
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))