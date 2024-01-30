
array = [i for i in range(1, 31)]

for i in range(28) :
    submitted = int(input())
    array[submitted-1] = 0

array = sorted(array)
print(array[30-2])
print(array[30-1])