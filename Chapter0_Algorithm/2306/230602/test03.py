"""
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.
예를 들어 코니가 가진 옷이 아래와 같고,
오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 
동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트

코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 
예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 
혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 
return 하도록 solution 함수를 작성해주세요.

>>> 입출력 예시
clothes	                                                        return
------------------------------------------------------------------------------------
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]	                                5
------------------------------------------------------------------------------------
[["crow_mask", "face"], ["blue_sunglasses", "face"], 
["smoky_makeup", "face"]]	                                    3
------------------------------------------------------------------------------------
"""

def solution(clothes):
    answer = 0
    clothes_sort = {}
    for name, type in clothes :
        print(name, type)
        if type not in clothes_sort :
            print("?")
            clothes_sort[type] = []
        clothes_sort[type].append(name)

    return clothes_sort

def solution(clothes):
    answer = 0
    clothes_sort = {}
    for name, type in clothes :
        print(name, type)
        if type not in clothes_sort :
            print("?")
            clothes_sort[type] = []
        clothes_sort[type].append(name)

    return clothes_sort


from itertools import combinations, permutations

arr = ["A", "A", "A"]

# 조합
print(list(combinations(arr, 2)))
# [(1, 2), (1, 3), (2, 3)]

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]	))

print("="*100)

"""
문제 이해 못하고 풀었음 다시 시도하기
"""
def solution(clothes):
    answer = 0
    clothes_sort = {}
    combination_store = []
    for name, type in clothes :
        print(name, type)
        if type not in clothes_sort :
            clothes_sort[type] = []
        clothes_sort[type].append(name)

    sort = 0
    for key, value in clothes_sort.items() :
        sort +=1
        print(key)
        print(value)
        #answer += len(value)
        combination_store +=[key]*len(value)

    for i in range(sort) :
        a = set(list(combinations(combination_store, i+1)))
        print(a)
        print(len(a))

    print(answer)
    return clothes_sort



"""
채점 결과
정확성: 96.4
합계: 96.4 / 100.0
>>> 시간 초과
"""
def multiply(arr):
    ans = 1
    for n in arr :
        if n == 0 :
            return 0
        ans *= n
    return ans


def solution(clothes):
    answer = 0
    clothes_sort = {}
    combination_store = []
    for name, type in clothes :
        if type not in clothes_sort :
            clothes_sort[type] = []
        clothes_sort[type].append(name)

    for key, value in clothes_sort.items() :
        combination_store.append(len(value))

    print(combination_store)

    for i in range(len(combination_store)) :
        l = list(combinations(combination_store, i+1))
        print(l)
        for arr in l :
            print(list(arr))
            value = multiply(list(arr))
            print(value)
            answer += value

    print(answer)
    return answer


def solution(clothes):
    ans=1
    clodict = {}
    for i in clothes:
        clodict[i[-1]]=0
    
    print(clodict)

    for k in clothes:
        clodict[k[-1]]+=len(k[:-1])

    print(clodict)

    for h in clodict.values():
        ans=(h+1)*ans
        print(h, ans)
        
    return ans-1

# 다른 사람 풀이 1
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


# 다른 사람 풀이 2
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], 
["green_turban", "headgear"]]	))