"""

"""

chess_basic_count  = [1, 1, 2, 2, 2, 8]

chess_I_have = input().split(" ")

result = []

for i in range(6) :
    n = chess_basic_count[i]-int(chess_I_have[i])
    result.append(n)

print(" ".join(map(str, result)))
