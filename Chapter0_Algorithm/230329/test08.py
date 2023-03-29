def solution(n, s):
    answer = []
    max = 0
    for i in range(1, s//2+1) :
        answer.append([i, s-i])

    if len(answer) == 0 :
        result = [-1]
    else :
        for a, b in answer :
            print(a, b)
            if (a*b) > max :
                result = [a, b]

    return result

print(solution(2,9))
print(solution(2,1))
print(solution(2,8))

print()
print("#"*30)
def solution1(n, s):
    answer = []
    if s // n <= 0: return [-1]
    answer = [s // n for _ in range(n)]
    if s % n == 0:
        # print(answer)
        return sorted(answer)
    for i in range(s % n):
        # print(answer)
        answer[i] += 1
    return sorted(answer)

# print(solution1(2,9))
# print(solution1(2,1))
# print(solution1(2,8))
print(solution1(3,10))

print()
print("#"*30)
print()


def solution2(n, s):
    if s < n:
        return [-1]
    answer = []

    for _ in range(n - s % n):
        print("="*15)
        answer.append(s // n)
        print(answer)
    for _ in range(s % n):
        print("="*15)
        answer.append(s // n + 1)
        print(answer)
    return answer


print(solution2(2,9))
print(solution2(2,1))
print(solution2(2,8))


print("\n\n\n\n")
s = 2
n = 9
answer = [s//n for _ in range(n)]
print(answer)


def solution4(n, s):
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n

    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer


def solution5(n, s):
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n
    print(f"b : {b}")
    
    for i in range(n-b):
        print(f"n-b : {n-b}")
        print(f"i : {i}")
        answer.append(a)
        print(f"a : {a}")
        print(f"answer : {answer}")
    for i in range(b):
        print(f"n-b : {b}")
        print(f"i : {i}")
        answer.append(a+1)
        print(f"a : {a}")
        print(f"answer : {answer}")

    return answer


print("="*20)
print(solution5(2,9))
print("="*20)
print(solution5(2,1))
print("="*20)
print(solution5(2,8))
print("="*20)
print(solution1(3,10))
print("="*20)
print(solution1(4,100))
print("="*20)
print(solution1(7,100))
print("="*20)