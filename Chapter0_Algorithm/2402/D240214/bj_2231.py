
n = int(input())

check = False

for i in range(1, n) :
    num_list = list(str(i))
    num_list.append(str(i))

    sum_list = list(map(int, num_list))
    if(sum(sum_list) == n):
        check = True
        print(i)
        break

if not check :
    print(0)

