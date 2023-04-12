"""
>>> pip3 install --upgrade pip
>>> python3 -m pip install numpy

하단 왼쪽에 파이썬 버전을 클릭해 준 후
인터프린터를 바꿔준다.
"""
# import numpy as np
import numpy as np
def productMatrix(A, B):

    return (np.matrix(A)*np.matrix(B)).tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]]
b = [[ 3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a,b)))