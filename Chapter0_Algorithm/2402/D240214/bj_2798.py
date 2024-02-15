# from itertools import combinations
# from itertools import permutations

# N, M = list(map(int, input().split(" ")))

# cards = list(map(int, input().split(" ")))

# cards.sort()

# print(M//3)
# print(cards)
# sum_list = []
# first_idx = 300000
# idx = 0
# for i in range(len(cards)) :
#     if first_idx >= abs(M-cards[i]) :
#         first_idx = M-cards[i]
#         idx = i

# print(first_idx)
# print(idx)

# print(138+181+185)
# print(181+185+214)

# com = list(combinations(cards, 3))
# for c in com :
#     if sum(c) == M :
#         print(sum(c))
#         break
#     else :
#         sum_list.append(abs(M-sum(c)))

# print("="*20)
# print(M-min(sum_list))


from itertools import combinations

N, M = list(map(int, input().split(" ")))

cards = list(map(int, input().split(" ")))
sum_list = []
check_point = True

com = list(combinations(cards, 3))
for c in com :
    if sum(c) == M :
        print(sum(c))
        check_point = False
        break
    else :
        if sum(c) <= M :
            sum_list.append(sum(c))


if check_point :
    print(max(sum_list))
