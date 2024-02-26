import sys

n = int(input())
cards = list(map(int, input().split(" ")))

dict = {}

for card in cards :
    if card not in dict :
        dict[card] = 1
    else :
        dict[card] +=1

m = int(input())
cards2 = list(map(int, input().split(" ")))

for card in cards2 :
    if card not in dict :
        print(0, end=" ")
    else :
        print(dict[card], end=" ")

# print(dict)

# list(dict.keys())