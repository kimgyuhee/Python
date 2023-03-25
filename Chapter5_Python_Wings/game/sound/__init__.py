"""
이렇게 특정 디렉터리의 모듈을 *를 사용하여 import할 때에는
다음과 같이 해당 디렉터리의 __init__.py 파일에 __all__ 변수를 설정하고
import할 수 있는 모듈을 정의해 주어야 한다.
"""

__all__ = ['echo']
# 위의 코드가 없으면 에러 발생
"""
>>> echo.echo_test()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined
"""