"""
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 
return 하도록 solution 함수를 완성하세요.

입출력 예
number	        k	return
"1924" 	        2	"94"
"1231234"	    3	"3234"
"4177252841"	4	"775841"


그리디(Greedy) 알고리즘은 탐욕법이라고도 하며, 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미합니다.
일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구합니다.
그리디 알고리즘을 이용하면 매 순간 가장 좋아 보이는 것만 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않습니다.


"""
# 채점 결과
# 정확성: 8.3
# 합계: 8.3 / 100.0
def solution(number, k):
    answer = ''
    sort_number= sorted(number)
    print("sort_number" ,sort_number)
    print("len(number)-k", len(number)-k)
    remove_num = sort_number[len(number)-k-1]
    list_number = list(number)
    print(remove_num)
    for i in range(len(list_number)) :
        if k == 0 :
            break
        if int(list_number[i]) <= int(remove_num) :
            k -=1
            list_number[i] = -1

    print("k",k)
    for n in list_number :
        if n != -1 :
            answer+=n
    return answer

print(solution("10000009", 8))
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("9929191", 5))


def solution(number, k):
    number = ''
    sort_number= sorted(number)
    remove_num = sort_number[len(number)-k-1]
    list_number = list(number)
    print(remove_num)
    while k != 0 :
        sort_number= sorted(number)
        remove_num = sort_number[len(number)-k-1]
        list_number = list(number)
        for i in range(len(list_number)) :
            if k == 0 :
                break
            if int(list_number[i]) <= int(remove_num) :
                k -=1
                list_number[i] = -1

        for n in list_number :
            if n != -1 :
                number+=n
    return number

print("="*20)
print("="*20)
def solution(number, k):
    answer = ""
    number_list = list(number)
    # max_idx = number_list.index(max(number_list))
    # max_index = number.index(max(number))
    # print(max_index)
    # print(number_list[max_idx:])
    # number_list = number_list[max_idx:]
    # print(number)
    while k!=0 :
        result = ""
        max_idx = number_list.index(max(number_list))
        print(max_idx)
        number_list = number_list[max_idx:]
        print(number_list)
        if max_idx > k :
            number_list_a = list(number)[:max_idx]
            #print(number_list_a)
            for i in range(k) :
                #print(i)
                remove_idx = number_list_a.index(min(number_list_a))
                number_list_a[remove_idx] = "10"
                #print(number_list_a)

            answer = number_list_a + number_list
        else :
            k -= max_idx
            for _ in range(k) :
                remove_idx = number_list.index(min(number_list))
                number_list[remove_idx] = "10"

            answer = number_list
        
        for a in answer :
            if a != "10" :
                result +=a
        break

    return result

def solution(number, k):
    answer = []

    for i in number:
        print(f"{i} 들어갑니다 ~")
        if not answer:
            print("리스트에 뭐가 있구만 !")
            answer.append(i)
            continue
        print(answer[-1], "<" , i)
        while answer[-1] < i and k > 0:
            print("아직 제거해야할게 남았구만")
            print(answer)
            print(f"{answer[-1]}, {i}")
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                print("이제 다 제거했구만 ! ")
                break

        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)

print(solution("41120566", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("9929191", 5))