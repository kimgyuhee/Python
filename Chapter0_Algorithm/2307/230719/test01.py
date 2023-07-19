"""
정수로 이루어진 배열 numbers가 있습니다. 
배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 
자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.
"""

# 채점 결과
# 정확성: 39.1
# 합계: 39.1 / 100.0
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1) :
        value = numbers[i]
        comparisonValues  = numbers[i+1:]
        find = -1
        for n in comparisonValues :
            if n > value :
                find = n
                break
        answer.append(find)
    answer.append(-1)
    return answer


def solution(numbers):
    print(numbers)
    answer = [-1] * len(numbers)
    backMax = numbers[-1]
    for i in range(len(numbers)-2,-1,-1):
        print(f"numbers[{i}] >= backMax {numbers[i]} {backMax}")
        if numbers[i] >= backMax:
            print("들어옴")
            backMax = numbers[i]
            print(backMax)
            continue
        
        print("="*10)
        for j in range(i+1,len(numbers)):
            print(numbers[j], numbers[i], answer[j])
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break    
            if numbers[i] >= numbers[j] and numbers[i] < answer[j]:
                answer[i] = answer[j]
                break


    return answer


print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]