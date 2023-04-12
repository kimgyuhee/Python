"""
# 1로 만들기 문제
"""
def solution(x) :

    d = [0] * 30001

    for i in range(2, x+1) :
        print(d[:30])
        print(d[i])
        d[i] = d[i-1] + 1
        if i % 2 == 0 :
            d[i] = min(d[i], d[i//2]+1)

        if i % 3 == 0 :
            d[i] = min(d[i], d[i//3]+1)

        if i % 5 == 0 :
            d[i] = min(d[i], d[i//5]+1)

    print(f"{x} --------> d[x] = {d[x]}")

solution(26)
solution(1)
solution(2)
solution(3)
solution(2)
solution(5)