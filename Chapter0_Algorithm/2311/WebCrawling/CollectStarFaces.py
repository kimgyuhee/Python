import install_development_environment
from selenium import webdriver 
# import chromedriver_autoinstaller
import time
import os
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def driverOpen(url) :
    query_txt = input('검색할 단어를 입력해주세요 : ')

    #Step 1. 크롬 드라이버를 이용해서 웹 브라우저를 연다.
    myProjectPath = os.path.dirname(os.path.realpath(__file__))
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    element = driver.find_element(By.NAME, 'q')
    element.send_keys(query_txt)                #검색 단어를 입력한다
    element.send_keys(Keys.RETURN)              #검색창 엔터 -> 결과
    
    return driver, query_txt


def scroll_webpage(driver) :
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, 5000);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height

def ImageDownload1(driver, query_txt) : #CASE1
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 1

    for image in images:
        try:
            if count <= 20 :
                imagePath = os.getcwd() + "/WebCrawling/Data/Trainig_Data/"
            elif count <= 25 :
                imagePath = os.getcwd() + "/WebCrawling/Data/Testing_Data/"
            else :
                break


            image.click()
            time.sleep(0.5)
            
            imgUrl = driver.find_element(
                By.XPATH,
                '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]'
            ).get_attribute("src")

            # opener = urllib.request.build_opener()
            # opener.addheaders = [
            #     ('User-Agent',
            #     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')
            # ]
            # urllib.request.install_opener(opener)
            
            urllib.request.urlretrieve(imgUrl, f'{imagePath}{query_txt}{str(count)}.jpg')
            count = count + 1

        except Exception as e:
            print("흑 속상해,,,")
            print('e : ', e)
            pass

def createFoler(directory) :

    Trainig_Data_Path = "./WebCrawling/Data/Training_Data/"
    Testing_Data_Path = "./WebCrawling/Data/Testing_Data/"
    
    try :
        print(f"{directory} 폴더가 없어서 생성합니다.")
        if not os.path.exists(Trainig_Data_Path + directory) :
            os.makedirs(Trainig_Data_Path + directory)
        if not os.path.exists(Testing_Data_Path + directory) :
            os.makedirs(Testing_Data_Path + directory)
        else :
            print(f"{directory} 폴더가 이미 존재합니다.")
    except OSError :
        print("method error")


driver, query_txt = driverOpen("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
createFoler(query_txt)
scroll_webpage(driver)
ImageDownload1(driver, query_txt)

driver.close()

