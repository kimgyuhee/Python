
arrays = []
max = 0
for i in range(5) :
    str = list(input())
    if max < len(str) :
        max = len(str)
    arrays.append(str)

result = ""

for i in range(5) :
    f = max - len(arrays[i])
    for j in range(f) :
        arrays[i] += [""]

for j in range(max) :
    for i in range(5) :
        if j < len(arrays[i]) :
            result += arrays[i][j]

print(result)
