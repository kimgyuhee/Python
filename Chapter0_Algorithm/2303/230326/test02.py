def solution(H, C):
    nowIndex = 0

    for i in C :
        print(f"{i} -> nowIndex : {nowIndex}")
        print(len(H))
        print(i)
        print(type(i))
        print(i == "NEXT")
        if i == "NEXT" :
            if nowIndex < len(H)-1 :
                print("+")
                nowIndex += 1
        else :
            if nowIndex < len(H) and nowIndex > 1 :
                print("-")
                nowIndex -=1

    answer = H[nowIndex]
    return answer

H = ["www.google.com",
"www.yahoo.com",
"www.midasit.com"]
H = ["www.google.com"]
C = ["BACK","BACK","NEXT"]
C = ["BACK","NEXT","NEXT","NEXT","NEXT","NEXT","NEXT", "BACK"]
C = ["NEXT"]
print(solution(H,C))