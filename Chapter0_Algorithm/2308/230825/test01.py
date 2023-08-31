"""
2개 이하로 다른 비트

양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.
x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

f(2) = 3 입니다. 
다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 
제일 작은 수가 3이기 때문입니다.

수	비트	        다른 비트의 개수
2	000...0010	
3	000...0011	  1

"""

q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
for i in range(18, 40) :
    q.append(i)
# 채점 결과
# 정확성: 81.8
# 합계: 81.8 / 100.0

def longValue(a, b) :
    if a >= b :
        return len(a)
    else :
        return len(b)

def compareBit(value) :
    other = value+1
    value_ = bin(value)[2:]
    while(True) :
        count = 0
        other_ = bin(other)[2:]
        value_ = value_.zfill(len(other_))
        for i in range(len(other_)) :
            if other_[i] != value_[i] :
                count +=1
            if count > 2 :
                continue
        if count == 1 or count == 2 :
            break

        other +=1

    return other
    

def solution(numbers):
    result = []
    for n in numbers :
        result.append(compareBit(n))
    return result


print(solution(q))


def compare1(value, other) :
    result = bin(value^other)

    diff = result.count('1')
    if diff == 1 or diff == 2 :
        return True
    
    return False

def solution(numbers):
    answer = []
    for i in numbers :
        if i%2 == 0 :
            number = i+1
        else :
            number = i
            while True :
                number +=1
                if compare1(i, number) :
                    break
        answer.append(number)

    return answer


def binary(value, other) :
    print(value, other)
    count = 0
    v = ""
    o = ""
    while True :
        va = value // 2
        vb = value % 2

        oa = other // 2
        ob = other % 2

        v +=str(vb)
        o +=str(ob)

        if v!= o :
            count +=1

        if va == 0 and oa == 0 :
            break
        else :
            value = va
            other = oa

    return count
    
def solution(numbers) :
    result = []
    for n in numbers :
        if n%2 == 0 :
            result.append(n+1)
        else :
            m = n
            while(True) :
                m +=1
                count = binary(n, m)
                if count == 1 or count == 2 :
                    result.append(m)
                    break
    return result

def binary(value) :
    n = 0
    num = 0
    for v in value[::-1] :
        if v == '1' :
            num +=2**n
        n+=1
    print("="*20)
    print(f"이진수 {value}는 십진수로 변환하면 {num} 입니다.")
    print("="*20)
    return num

def solution(numbers) :
    result = []
    for n in numbers :
        print(n, "을 변환해보아여 !")
        if n%2 == 0 or n == 1:
            print("짝수 또는 1이라 n에 1을 더해줍니다.\n")
            result.append(n+1)
        else :
            m = n
            n_bin = bin(m)[2:]
            index0 = n_bin[::-1].find("0")
            if index0 == -1 :
                print("->",n,"의 이진수는 모두 1로 이루어져 있습니다.\n")
                print('10'+n_bin[1:])
                num  = binary('10'+n_bin[1:])
                # index1 = n_bin[::-1].find("1")
            else :
                n_bin = n_bin[::-1].replace("0", "1", 1)
                n_bin = n_bin.replace("1", "0", 1)
                num = binary(n_bin[::-1])
            result.append(num)
                        
    return result

print(solution(q))

def solution(numbers):
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]


def solution(numbers):
    answer = []

    def toBinary(number):
        ans = ''
        while number > 0:
            ans += str(number%2)
            number = number//2

        add_zero = 4-(len(ans)%4)
        ans += '0' * add_zero

        return ans[::-1]

    def toDecimal(number):
        ans = 0; l = len(number)-1
        for n in number:
            ans += (2**l)*int(n)
            l -= 1

        return ans

    for num in numbers:
        if num%2 == 0:
            answer.append(num+1)
        else:
            odd_to_binary = toBinary(num)

            for i in range(len(odd_to_binary)-1, -1, -1):
                if odd_to_binary[i] == '0':
                    odd_to_binary = odd_to_binary[:i] + '10' + odd_to_binary[i+2:]
                    answer.append(toDecimal(odd_to_binary))
                    break

    return answer




def f(number):
    bin_num = bin(number)[2:]

    if '0' not in bin_num:
        return int('10' + bin_num[1:], 2)

    bin_num = list(bin_num)
    for i in range(len(bin_num)):
        print(-i-1)
        if bin_num[-i-1] == '0':
            bin_num[-i-1] = '1'
            break

    if i > 0:
        bin_num[-i] = '0'

    return int(''.join(bin_num), 2)


def solution(numbers):
    answer = [f(number) for number in numbers]
    return answer

print(solution(q))
print(q)
