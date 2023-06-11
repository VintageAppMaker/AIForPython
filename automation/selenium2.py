# selenium1.py의 소스로 다음과 같은 프롬프트를 GPT에게 던졌다. 

# 1. chrome 드라이버를 소스가 존재하는 경로에 저장했습니다. 
# 2. www.google.com에 가서 "Vintage appMaker"를 검색합니다. 
# 3. 결과 화면을 capture.png로 저장합니다. 
# 소스를 만들어주세요

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver의 경로를 지정합니다.
webdriver_path = 'c:\\github\\chromedriver.exe'

# Chrome WebDriver를 생성합니다.
driver = webdriver.Chrome(executable_path=webdriver_path)

# Google 홈페이지를 방문합니다.
driver.get('https://www.google.com')

# 검색어를 입력합니다. <- code를 분석하고 viantage appMaker가 수정함
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Vintage appMaker')
search_box.send_keys(Keys.ENTER)

# 📣 대기를 하지 않으면 검색결과 이전의 화면을 저장한다.
# codium에게 프롬프트해서 얻은 함수
# 페이지가 완전히 로드될 때까지 기다림 (10초가 넘어가면 TimeoutException 발생)
wait = WebDriverWait(driver, 10)
page_loaded = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# 결과 화면을 capture.png로 저장합니다.
driver.save_screenshot('capture.png')
