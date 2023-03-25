# from game.sound import echo
# from sound import echo

# from game.sound.echo import echo_test # CASE1
from ..sound.echo import echo_test # CASE2
def render_test():
    print("render")
    echo_test()

# 여기서 디버깅 실행하면 에러
""" 터미널에서
>>> from game.graphic.render import render_test
>>> render_test()
render
echo

..  – 부모 디렉터리
.   – 현재 디렉터리
"""