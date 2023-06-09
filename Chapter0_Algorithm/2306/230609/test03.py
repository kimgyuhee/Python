"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 
그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

문제를 완벽하게 이해하지 못한 나는 바보이다....
"""
# 채점 결과
# 정확성: 66.7
# 효율성: 8.3
# 합계: 75.0 / 100.0
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book)) :
        value = phone_book[i]
        print(value)
        for number in phone_book[i+1:] :
            if value in number :
                return False
    return answer


def solution(phone_book):
    answer = True
    books = []
    phone_book.sort(key=len)
    for v in phone_book :
        books.append("".join(v))
    for i in range(len(phone_book)) :
        value = books[i]
        for number in books[i+1:] :
            if value in number :
                return False
    return answer


def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book)-1) :
        value = phone_book[i]
        for number in phone_book[i+1:] :
            if value in number :
                return False
    return answer


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        print(f"{'='*10} i는 현재 {i}입니다. {'='*10}")
        print(phone_book[i+1][:len(phone_book[i])])
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])] :
            return False
    return True

# print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","78900123"]))
print(solution(["456","789", "12", "123"]))
# print(solution(["1", "444356", "4444", "44445"]))