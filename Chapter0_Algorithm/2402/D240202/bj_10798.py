
arrays = []

for i in range(5) :
    str = list(input())
    arrays.append(str)

result = ""

for i in range(5) :
    for j in range(len(arrays[i])) :
        try :
            result += arrays[j][i]
        except(IndexError) :
            result +=""

print(result)