"""

그린은 유치원생인 레드와 블루에게 수학을 가르치고 있다.
 그린은 수학을 더 재밌게 배울 수 있도록 둘에게 간단한 게임을 시켰는데, 
 어떤 정수를 하나 고르면 레드와 블루가 계산 결과가 그 정수가 나오도록 계산 식을 만드는 것이다.
   레드와 블루는 아직 수학에 대해 그렇게 잘 알지는 못하기 때문에, 둘이 만든 식은 모두 다음의 조건을 만족한다.

덧셈(+), 뺄셈(-) 이외의 연산자는 등장하지 않는다.
음수나 억 이상의 단위를 알지 못하기 때문에, 계산 식에 등장하는 모든 수는 0 이상 10^8 미만의 정수이다.
계산 식을 앞에서부터 차례대로 계산할 때, 계산 과정에서 나타나는 모든 수도 0 이상 10^8 미만의 정수이다. 물론 계산을 모두 끝냈을 때 나오는 수도 포함한다.
예를 들어 "1+2+3"의 계산 과정에서 나타나는 수는 1, 3, 6 이다.
계산 식에 등장하는 모든 수는 앞에 불필요한 0 (leading zero)를 포함하지 않는다. 즉, 수가 0으로 시작하는 경우는 오직 0밖에 없다.
식에는 최소 하나의 숫자가 포함되어 있다. 연산자(+ 혹은 -)는 포함되어있지 않을 수 있다.
둘이 만든 식의 계산 결과는 동일하다.
"""

from itertools import combinations


def solution(S) :
    s = list(S)
    opt = []
    num = []
    index = 0
    for i in s :
        if i == "+" or i == "-" :
            opt.append(i)
        else :
            num.append(int(i))


    if len(opt) > 0 :
        result = []
        for i in range(0, len(num)//len(opt)) :
            combiN = list(combinations(num, len(opt)))
            for i in range(0, len(combiN)//2) :
                result.append([[combiN[i], opt[1]],[combiN[-(i+1)], opt[0]]])

        def samecheck(a, b) :
            # print(cal(a[0], a[1]), cal(b[0], b[1]), cal(a[0], a[1]) == cal(b[0], b[1]))
            if cal(a[0], a[1]) == cal(b[0], b[1]) :
                return True
            else :
                return False

        def cal(n, o) :
            # print("dhd")
            if o == "-" :
                return n[0]-n[1]
            elif o == "+" :
                return n[0]+n[1]
            else :
                print("기호가 잘못되었습니다.")

        # print(result)    
        for r in result :
            if samecheck(r[0], r[1]) :
                index +=1

        
        return index

    # S문자열에 기호가 존재하지 않을때
    count = 0
    if len(opt) == 0 :
        if len(S)%2 != 0 :
            return 0
        else :
            combi = list(combinations(S, len(S)//2))
            for i in range(0, len(combi)//2) :
                if combi[i] == combi[-(i+1)] :
                    count +=1

            return count * 2



print("결과는 ? ",solution("16-+23"))

print("결과는 ? ", solution("111111"))
print("결과는 ? ",solution("1111"))
print("결과는 ? ",solution("1221"))