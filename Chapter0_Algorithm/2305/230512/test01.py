"""
정수 배열 arr이 매개변수로 주어집니다. 
arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. 
arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.
"""
# 합계: 68.2 / 100.0
def solution(arr):
    len_arr = [1,2,4,8,16,32,64,128,256,512,1000]
    for i in range(len(len_arr)) :
        if len_arr[i] >= len(arr) :
            n = i
            break
    return arr + [0]*(len_arr[n]-len(arr))

print(solution([58]))
print(solution([58, 172, 746, 89]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1,1,2,3,4,5,6,7,8,10,10]))
print(solution([1,2,3,4,5]+[1]*994))

