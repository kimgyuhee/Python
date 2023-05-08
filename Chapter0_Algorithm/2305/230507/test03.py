"""
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 
길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, 
flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고, 
flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.

"""

def solution(arr, flag):
    answer = []
    for a, f in zip(arr, flag) :
        if f :
            answer+=[a]*2*a
        else :
            answer = answer[:-a]
    return answer

ad = 2
print([ad]+[])
d =[0,1,2,3,4,5,6,7,8]
print(d[:-2])

