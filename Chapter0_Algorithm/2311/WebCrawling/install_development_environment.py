import os # 운영체제 종속 기능에 대한 간단한 명령을 모아놓은 기본 모듈
import sys # 파이썬 인터프리터와 관련된 정보 기능을 제공하는 모듈
import subprocess  # 쉘 명령을 실행할수있게 해주는 라이브러리


try :
    import pip
    print('pip 버전 : ' + pip.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    print('pip 모듈을 설치하였습니다.\npip : ' + pip.__version__)

try :
    from bs4 import BeautifulSoup
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'bs4'])
    print('bs4 모듈을 설치하였습니다.\n')

try :
    import selenium
    print('selenium 버전: ' + selenium.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'selenium'])
    print('selenium 모듈을 설치하였습니다.\n')

try :
    import chromedriver_autoinstaller
    print('chromedriver_autoinstaller 버전: ' + chromedriver_autoinstaller.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'chromedriver_autoinstaller'])
    chromedriver_autoinstaller.install()
    print('chromedriver_autoinstaller 모듈을 설치하였습니다.\n')

try :
    import requests
    print('requests 버전: ' + requests.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    print('requests 모듈을 설치하였습니다.\n')
    
print('\n')
print('모듈 버전 검사를 마쳤습니다.')
