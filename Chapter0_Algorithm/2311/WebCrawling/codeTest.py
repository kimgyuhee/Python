from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

chrome_options = webdriver.ChromeOptions()
chrome_options.binary = '/Users/gyuhee/Downloads/chromedriver_mac_arm64/chromedriver' # 드라이버 실행파일 경로

query = '춘식이'

driver = webdriver.Chrome()
driver.get(f'https://www.google.com/imghp')
search_bar = driver.find_element(By.NAME,"q")
search_bar.send_keys(query)
search_bar.submit()

PAUSE_TIME = 2
last_hegiht = driver.execute_script("return document.body.scrollHeight")
new_height = 0

while True :
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height - last_hegiht > 0 :
        last_hegiht = new_height
        continue
    else :
        break

img_elements = driver.find_elements(By.CSS_SELECTOR,".rg_i")
imgs = []

for idx, img in enumerate(img_elements) :
    print(f"{query} : {idx+1}/{len(img_elements)} proceed...")
    try :
        img.click()
        time.sleep(PAUSE_TIME)
        # 이부분에서 에러나면, 직접 개발자 도구 활용해서 XPATH 추출한 뒤에 변경
        img_element = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[2]/div[1]/a/img[1]')
        img_src = img_element.get_attribute('src')
        img_alt = img_element.get_attribute('alt')
        imgs.append({
            'alt' : img_alt,
            'src' : img_src
        })
        
    except :
        print(f'err in {idx}')
        pass

driver.close()

save_path = f'.\{query}'
import os
if not os.path.exists(save_path):
    os.mkdir(save_path)

total_N = len(imgs)
for idx, one in enumerate(imgs):
    src = one['src']
    alt = one['alt']
    urllib.request.urlretrieve(src,  f"{save_path}\{query}_{idx}.png")
    print(idx, alt)

print('done')