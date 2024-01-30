
str_input = input("A, B, C를 순서대로 입력하시오. -> ")

array = str_input.split()
result = 0

for a in array :
    result += int(a)

print(result)
