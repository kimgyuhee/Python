
words = [0, 1, 2, 3, 4, 5, 6,7,8,9]
for i in range(26) :
    words += [chr(65+i)]

def convert(n, digit) :
    tmp = ""
    while n :
        if n%digit >= 10 :
        # print(words[n % digit], n % digit)
            tmp += words[n % digit]
        else :
            tmp += str(n%digit)
        n = n // digit
    return tmp[::-1]


N, digit = list(map(int, input().split(" ")))

print(convert(N, digit))