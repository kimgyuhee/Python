"""
복습
"""

from itertools import permutations

def solution(k, dungeons) :
    cases =  permutations(dungeons,len(dungeons))
    results = []
    for case in cases :
        now_ph = k
        result = 0
        for ph, attack in case :
            if now_ph >= ph :
                result +=1
                now_ph -=attack
        
        results.append(result)
    
    return max(results)

print(solution(80,[[80,20],[50,40],[30,10]]))



from itertools import permutations

def solution(k, dungeons):

    all_dungeons = []
    for i in permutations(dungeons,len(dungeons)):
        all_dungeons.append(list(i))
    
    case = []
    for dungeon in all_dungeons :
        value = 0
        now_ph = k
        #print(dungeon)
        for minimal_ph, ph in dungeon :
            if now_ph >= minimal_ph :
                now_ph = now_ph-ph
                value +=1
        #print(value)
        case.append(value)

    return max(case)