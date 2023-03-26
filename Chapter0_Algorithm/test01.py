def solution(n, m, a, b, c, d):
    answer = ''
    return answer






def checkIntInput(a, b) :
    while 1:
        try :
            n = int(input("입력해봐")) #정점의 개수
        except ValueError :
            print("숫자를 입력해주세요 :)"); continue
        else :
            if not(n >=a and n<=b) :
                print(f"{a}~{b} 사이의 숫자를 입력해주세요.")
                continue
            else :
                break
    return n

n = checkIntInput(1, 20000)

print(n)
    # if n.isdigit() :
    #     print(n)
    #     n = int(n)
    #     print(type(n))
    #     return n
    # else :
    #     if n.find('-'):
    #         print(n)
    #         n = int(n)
    #         print(type(n))
    #         return n
    #     else :
    #         return -1


# while True :
#     n = checkIntInput()
#     if n >=1 and n<=20000 : # n의 범위
#         break 