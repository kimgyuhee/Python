"""
파일명 정렬
세 차례의 코딩 테스트와 두 차례의 면접이라는 기나긴 블라인드 공채를 무사히 통과해 
카카오에 입사한 무지는 파일 저장소 서버 관리를 맡게 되었다.

저장소 서버에는 프로그램의 과거 버전을 모두 담고 있어, 
이름 순으로 정렬된 파일 목록은 보기가 불편했다. 
파일을 이름 순으로 정렬하면 나중에 만들어진 ver-10.zip이 ver-9.zip보다 먼저 표시되기 때문이다.

버전 번호 외에도 숫자가 포함된 파일 목록은 여러 면에서 관리하기 불편했다. 
예컨대 파일 목록이 ["img12.png", "img10.png", "img2.png", "img1.png"]일 경우, 
일반적인 정렬은 ["img1.png", "img10.png", "img12.png", "img2.png"] 순이 되지만, 
숫자 순으로 정렬된 ["img1.png", "img2.png", "img10.png", img12.png"] 순이 훨씬 자연스럽다.

무지는 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.

소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 
영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 
파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.
"""

# 채점 결과
# 정확성: 90.0
# 합계: 90.0 / 100.0
import re

def solution(files):
    storedFiles = []
    answer = []

    for i, file in enumerate(files) :
        file = file.lower()
        p = re.compile('[0-9]+')
        fineNumber = p.findall(file)
        number = fineNumber[0]
        l = file.split(number)
        l.insert(1, int(number))
        l.insert(0, i)
        storedFiles.append(l)

    result = sorted(storedFiles, key=lambda x: (x[1], x[2], x[0])) # 0번, 1번 키(알파벳, 숫자)
    
    for i in result :
        answer.append(files[i[0]])

    return answer


import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b


"""
입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
"""
print(solution(["abc123defg123.jpg","img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

"""
입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
"""

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat", "F-15"]))