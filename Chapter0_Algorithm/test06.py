def solution(babbling):
    answer = 0
    index = 0
    possible = ["aya", "ye", "woo", "ma"]
    for b in babbling :
        for p in possible :
            if b.find(p) != -1:
                babbling[index] = babbling[index].replace(p , "")
                continue
        index +=1

    # print(babbling)

    for b in babbling :
        if b == "":
            answer +=1
    return answer



print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
print(solution(["ayawoomaye"]))