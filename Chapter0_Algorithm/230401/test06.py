"""
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다.
영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
이전에 등장했던 단어는 사용할 수 없습니다.
한 글자인 단어는 인정되지 않습니다.
다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
(계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.
"""
def solution(n, word) :
    count = 0
    word_record = []
    divide = {i : [] for i in range(n)}
    for w in range(len(word)//n) :
        divide[(w*n)%n].append(word[(w*n)])
        divide[(w*n+1)%n].append(word[n*w+1])
        divide[(n*w+2)%n].append(word[n*w+2])

    index = 0
    for w in word :
        if index%n == 0 :
            count +=1
            
        if w in word_record :
            break
        else :
            print(word[index+1], w)
            print(index, word[index+1][0], w[-1])
            if word[index+1][0] != w[-1] :
                break
            word_record.append(w)
            index +=1
    
    if len(word) == index :
        return [0,0]
    else :
        return [(index+1)//n, count]



print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


a = ["hello", "one", "even", "never", "now", "world", "draw"]
print(a[2][0])


print("위의 코드는 오류")

def solution(n, words) :
    count = 0
    index = 0
    word_list = []
    for i in range(0, len(words)-1) :
        print(f">>> count : {count}\n>>> index : {index}\n")
        print(f"i : {i}\nwords[i] : {words[i]}\nword_list : {word_list}")
        if words[i] in word_list :
            index = i
            print(words[i])
            break
        else :
            if words[i+1][0] != words[i][-1] :
                index = i
                print(words[index])
                break
            else :
                word_list.append(words[i])
                if (index+1)%n == 0 :
                    count+=1
                index +=1

    if index == len(words) :
        return [0,0]
    else :
        print(index, count, n)
        if (index+1)%n == 0 :
            index = n
        else :
            index = (index+1)%n
        return [index, count]

def solution(n, words):
    answer = [0, 0]
    idx = -1
    
    while idx + 1 < len(words):
        idx += 1
        if idx > 0 and words[idx-1][-1] != words[idx][0] or words[idx] in words[:idx]:
            answer = [(idx % n) + 1, idx // n + 1]
            break
    return answer
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
