"""
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 
썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 
따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 
썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 
가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.
"""

"""
자료구조 - Tree

"""

def solution(skill, skill_trees):
    comparative_value = ""
    for i in range(1, len(skill)+1) :
        comparative_value+=f"{i}"

    skill_dict = { skill[i] : f"{i+1}" for i in range(len(skill)) }
    answer = []

    for skill_tree in skill_trees :
        str_int = ""
        for s in skill_tree :
            if s in list(skill_dict.keys()) :
                str_int +=skill_dict[s]
            else :
                str_int +='0'

        value = str_int.replace('0', '')
        answer.append(value)
    
    result = 0
    for a in answer :
        value = True
        for i in range(len(a)) :
            if comparative_value[i] != a[i] :
                value = False
                break
        if value :
            result +=1
    
    return result

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2

# 다른 사람 풀이 
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            print(skill_list)
            if s in skill:
                ch = skill_list.pop(0)
                print(skill_list, s, ch)
                if s != ch:
                    print(f"{skills}는 나가리 ~")
                    break
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2