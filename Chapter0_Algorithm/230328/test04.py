"""
"""
answer = ''
ss = "AA"
s = 'a'
print(ss.lower())
print(ss.upper())
print(type(ord('a')))
if ord(s) >= ord('a') and ord(s) <= ord('z') :
    answer += s.upper()

def solution(my_string):
    return my_string.swapcase()
#>.....

rsp = "205"
print(list(rsp))

def solution(rsp):
    answer = ''
    vs = {"2" : "0", "0" : "5", "5" : "2"}
    for r in list(rsp) :
        print(vs[r])
        answer += vs[r]
    
    print(answer)
    return answer

solution(rsp)

print("오잉?")
a = "abcd"
print(a[1])

print("오잉?")
def solution(cipher, code):
    answer = ''
    index = 0
    nowIndex = 0
    while len(cipher) > nowIndex +code:
        print(f"len(cipher) : {len(cipher)} / nowIndex : {nowIndex}")
        if len(cipher) < nowIndex :
            break
        # index +=1
        print(index)
        nowIndex = code*(index+1)-1
        answer += cipher[nowIndex]
        index  +=1
        print(index)
        print(answer)
        print(f"{nowIndex}, index : {index}, len(cipher) : {len(cipher)}")
    return answer

print(solution("dfjardstddetckdaccccdegk", 4))