
park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

def solution(park, routes):
    if(len(park)==0) :
        return 
    H = len(park)-1 #3
    W = len(park[0])-1 #2 ->
    for i in range(0, len(park)) :
        if "S" in park[i]:
            n = i #0
            m = park[i].index("S") #1

    print(n, m)
    print(H, W)

    def move(n, m, c) :
        print(f"현재 위치 : {n}, {m}")
        result = True
        for i in range(1,c+1):
            if park[n][m+i] == "X" :
                result = False
                break
        return result

    def moveUpandDown(n,m,c) :
        result = True
        print(f"현재 위치 : {n}, {m}")
        for i in range(1, c+1):
            if park[n+i][m] == "X":
                result = False
                break

        return result

    def position(point, n, m, c) :
        if point == "E" : # ->'=
            print(f"현재 위치 : {n}, {m}")
            print("값 확인")
            print(c+m, H)
            if (m+c) <= W :
                if move(n,m,c) :
                    m = m+c

        elif point == "W" : # <-
            if (m-c) >= 0 :
                if move(n,m-c,c) :
                    m = m-c
        elif point == "S" :
            if(n+c) <= H :
                if moveUpandDown(n,m,c):
                    n = n+c

        else :
            if(n-c) >= 0 :
                if moveUpandDown(n-c,m,c):
                    n = n-c

        return n, m

    for r in routes :
            point, c = r.split(" ")
            c = int(c)
            n, m = position(point, n, m ,c)
            print("움직인 결과" , n, m)

    print("정답" , n, m)
    return [n, m]


print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
print(solution(["OS"], ["W 1"]))
print(solution([], []))