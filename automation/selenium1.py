from selenium import webdriver

# Chrome WebDriver의 경로를 지정합니다.
webdriver_path = ''

# Chrome WebDriver를 생성합니다.
driver = webdriver.Chrome(executable_path=webdriver_path)

# Google 홈페이지를 방문합니다.
driver.get('https://www.google.com')

# 브라우저를 닫습니다.
driver.quit()
