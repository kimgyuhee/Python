"""
햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다. 
함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고, 
상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다. 
상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다. 
상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 
재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 
상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 
아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 
즉, 2개의 햄버거를 포장하게 됩니다.

상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

"""
from collections import deque

def solution(ingredient):
    perfect = [1, 2, 3, 1]
    answer = 0
    result = deque()
    for i in range(0, len(ingredient)) :
        index = 0
        result = deque()
        for i in ingredient :
            if i == 1 and (index == 0 or index == 3) :
                result.append(i)
                ingredient.remove(i)
                # index+=1
                if index == 3 :
                    answer+=1
                    index = 0
                    result = deque()
                else :
                    index+=1
            elif i == 2 and index == 1 :
                result.append(i)
                ingredient.remove(i)
                index+=1
            elif i == 3 and index == 2 :
                result.append(i)
                ingredient.remove(i)
                index +=1
            else :
                index = 0

    return answer


# 합계: 38.9 / 100.0 -> 시간초과
def solution(ingredient):
    answer = 0
    def checkHumberger(ingredient) : 
        perfect = [1, 2, 3, 1]
        result = []
        rest = []
        open = False
    
        for i in ingredient :
            print(f"{i}가 어디에 들어갈까요????")
            if result == perfect :
                rest.append(i)
                print(f"result : {result}\nrest : {rest}")
                continue
            if i == 1 :
                if not open :
                    open = True
                    result.append(i)
                else :
                    if len(result) == 3 :
                        result.append(i)
                        open = False
                    else :
                        rest.append(i)
            elif (i == 2 or i == 3) and open :
                result.append(i)            
            else :
                rest.append(i)
            print(f"result : {result}\nrest : {rest}")

        print(rest, result == perfect)
        return rest, result == perfect

    for i in range(0, len(ingredient)//4) :
        ingredient, ch = checkHumberger(ingredient)
        if ch :
            answer +=1

    return answer


def solution(ingredient):
    answer = 0
    print(ingredient)
    perfect = [1, 2, 3, 1]

    def pop(stack) :
        s = "".join(map(str, stack))
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        return stack
    
    p = "1231"
    stack = []
    for i in ingredient :
        print(f"{i}를 넣어볼게요 :) stack : {stack}")
        s = "".join(map(str, stack))
        if p in s :
            print("POPPOP")
            answer +=1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
        stack.append(i)
    s = "".join(map(str, stack))   
    if p in s :
            print("POPPOP")
            answer +=1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return answer


def solution(ingredient) :
    stack = []
    answer = 0
    for i in ingredient :
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1] :
            answer +=1
            for _ in range(4) :
                stack.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))


if [1, 2, 3, 4] in [1, 2, 3, 4, 5, 6] :
    print("dkdksdsajldksa") 

if "1234"in "123456" :
    print("dkdksdsajldksa") 

a = [1,2,3]
print("".join(map(str, a)))