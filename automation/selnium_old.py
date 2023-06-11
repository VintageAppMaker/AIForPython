import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 크롬에서 DOM 찾는법
# 1. shift + ctrl + c
# 마우스로 원하는 위젯클릭
# 소스코드로 이동

chrome_path = "C:\\github\\chromedriver.exe"

#  날씨가져오기
def doGetWeather():
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(executable_path=chrome_path, options=options)

    # 날씨검색
    browser.get("https://www.google.com/search?q=%EB%82%A0%EC%94%A8&sourceid=chrome&ie=UTF-8")
    time.sleep(3)

    # 날씨출력
    where   = browser.find_elements_by_xpath("//*[@id=\"wob_loc\"]")
    print("위치:" + where[0].text)
    curtime = browser.find_elements_by_xpath("//*[@id=\"wob_dts\"]")
    print("시간:" + curtime[0].text +"\n")

    temp = browser.find_elements_by_xpath("// *[ @ id = \"wob_tm\"]")
    print("온도:" + temp[0].text + "\n\n")

    browser.close()


def NaverVK():
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(executable_path=chrome_path, options=options)

    # blog 접속시 리다이렉션 되는 주소를 크롬에서 찾아보아야 한다.
    browser.get("https://naver.com")
    time.sleep(2)

    keys = [
        # 가상키보드 on/off
        "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div[1]/button[1]",

        # 마우스 입력으로 전환버튼  
        "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div[1]/div/div/span[3]/button",

        # 타이핑 ㄱ
        "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/span[1]/button",

        # 검색버튼
        "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/form/fieldset/button/span[1]"
 
    ]

    for k in keys:
        vk = browser.find_element_by_xpath(k)
        vk.click()
        time.sleep(1)


    time.sleep(2)
    browser.close()

# 함수테이블
fTable = [doGetWeather, NaverVK]

if __name__ == "__main__":
    for p in fTable:
         p()
