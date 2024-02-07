
coins = [25, 10, 5, 1]
counts = []
T = int(input())

for i in range(T):
    C = int(input())
    count = []
    for coin in coins :
        count.append(C//coin)
        C = C%coin
    counts.append(count)

for c in counts :
    print(" ".join(map(str, c)))
