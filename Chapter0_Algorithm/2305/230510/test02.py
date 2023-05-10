"""
문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 
가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(strArr):
    answer = 0
    result = {}
    for s in strArr :
        if len(s) not in result :
            result[len(s)] = 1
        else :
            result[len(s)] +=1
    
    sorted_dict = sorted(result.items(), key = lambda item: item[1], reverse = True)
    # print(sorted_dict)
    return sorted_dict[0][1]

print(solution(["a","bc","d","efg","hi"]))
dic = {2 : [32,1]}
print(1 not in dic)
print(2 not in dic)

# 다른 사람 풀이 1
def solution(strArr):
    a=[0]*31
    for x in strArr: a[len(x)]+=1
    return max(a)


# 다른 사람 풀이 2
def solution(strArr):
    w_len = [0 for _ in range(31)]
    for w in strArr:
        w_len[len(w)] += 1
    return max(w_len)