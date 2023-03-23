"""
파이썬 프로그래밍 기초, 자료형(숫자형)
"""
a = 123 # 정수형
b = 1.2 # 실수형

c = 0o177 # 8진수
cc = "0o177" # 8진수
d = 0x8ff # 16진수
e = 100
f = 3
print(a, b, c, d)
print(e//f) # 몫을 반환
print(float(e)//f)
print(float(e)//float(f))
def eightToten(cc) :


    print(f"{cc}를 10진수로 변경하면?")
    test_list1 = list(reversed(list(cc)))
    print(test_list1)
    """
    test_list = list(cc)
    print(test_list.reverse()) # None 이라는 결과가 나옴
    """

    result = 0 # 결과값 계산 변수

    for i in range(0, len(test_list1)-2) :
        value = int(test_list1[i])
        value = value*(8 ** i) # ** 은 제곱 연산자 
        result +=value
    print("8진수 -> 10진수")
    print(f"{cc} -> {result}")


eightToten(cc)


