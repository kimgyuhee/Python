def solution(array, height):
    return sum(1 for a in array if a > height)

print(solution([130,190, 186, 192], 168))

print(sum(1 for i in range(3)))

my_string = "hihi"
answer = my_string[::-1]
print(answer)


string = 'Hello, World!'
reversed_str = "".join(reversed(string))
print(reversed_str)

a = "asdfgh"
print(a.replace("g", ""))

def solution(my_string, letter):
    return my_string.replace(letter, '')

print(solution(string, "l"))

a = ['a', 'b', 'c', 'd', '1', '2', '3']
# 리스트를 문자열로 : join 이용
result1 = "".join(a)
print(result1)

a = ['BlockDMask', 'python', 'join', 'example']
print(a)
print()
 
# 리스트를 문자열로 합치기
result1 = "_".join(a)
print(result1)
 
# 리스트를 문자열로 합치기
result2 = ".".join(a)
print(result2)

f = [3,4,5,1,2,6,12,0]
f.sort()
print(f)

a= "fdsjflkqaaa"
print(sorted(a))

def solution(my_string, n):
    return ''.join(i*n for i in my_string)


def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

print(solution([1,4,5,7]))
"""
드래그는 바탕화면의 격자점 S(lux, luy)를 마우스 왼쪽 버튼으로 클릭한 상태로 격자점 E(rdx, rdy)로 이동한 뒤 마우스 왼쪽 버튼을 떼는 행동입니다. 이때, "점 S에서 점 E로 드래그한다"고 표현하고 점 S와 점 E를 각각 드래그의 시작점, 끝점이라고 표현합니다.

점 S(lux, luy)에서 점 E(rdx, rdy)로 드래그를 할 때, "드래그 한 거리"는 |rdx - lux| + |rdy - luy|로 정의합니다.

점 S에서 점 E로 드래그를 하면 바탕화면에서 두 격자점을 각각 왼쪽 위, 오른쪽 아래로 하는 직사각형 내부에 있는 모든 파일이 선택됩니다.

예를 들어 wallpaper = [".#...", "..#..", "...#."]인 바탕화면을 그림으로 나타내면 다음과 같습니다.

"""
print("\n"*3)
S = (0, 1)
E = (3, 4)


def solution(wallpaper):
    s = 100
    e = 0
    S, E = [], []
    pos = []
    answer = []
    index = 0
    for w in wallpaper :
        print()
        print(w)
        if "#" in w :
            pos.append([index, w.index("#")])
        print(pos)
        print(S)
        index +=1
    print(pos)
    index = 0
    for i, j in pos :
        print(i, j)
        if i < s :
            print("S")
            S = pos[index]
            s = i
            print(S)
        if j > e :
            print("E")
            E = pos[index]
            e = j
            print(E)

        index +=1

    print("dld?")
    print(S)
    print(E)
    print(S+E)
    return S+E


        
d = (abs(S[0]-E[0])+abs(S[1]-E[1]))

# print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
