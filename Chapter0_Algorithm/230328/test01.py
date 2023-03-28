def solution(array, height):
    return sum(1 for a in array if a > height)

print(solution([130,190, 186, 192], 168))

print(sum(1 for i in range(3)))

my_string = "hihi"
answer = my_string[::-1]
print(answer)


string = 'Hello, World!'
reversed_str = "".join(reversed(string))
print(reversed_str)

a = "asdfgh"
print(a.replace("g", ""))

def solution(my_string, letter):
    return my_string.replace(letter, '')

print(solution(string, "l"))

a = ['a', 'b', 'c', 'd', '1', '2', '3']
# 리스트를 문자열로 : join 이용
result1 = "".join(a)
print(result1)

a = ['BlockDMask', 'python', 'join', 'example']
print(a)
print()
 
# 리스트를 문자열로 합치기
result1 = "_".join(a)
print(result1)
 
# 리스트를 문자열로 합치기
result2 = ".".join(a)
print(result2)

f = [3,4,5,1,2,6,12,0]
f.sort()
print(f)

a= "fdsjflkqaaa"
print(sorted(a))

def solution(my_string, n):
    return ''.join(i*n for i in my_string)


def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

print(solution([1,4,5,7]))