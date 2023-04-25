from collections import Counter

c = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
cc = Counter("hello world")
print(list(c))
print(cc)

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

a = countLetters('hello world')
print(a)

"""
산술 연산자 활용
Counter가 재밌는 부분은 바로 마치 숫자처럼 산술 연산자를 사용할 수 있다는 것인데요.
예를 들어, 아래와 같이 2개의 카운터 객체가 있을 때,
"""
counter1 = Counter(["A", "A", "B"])
counter2 = Counter(["A", "B", "B"])

c = counter1 + counter2
print(c)