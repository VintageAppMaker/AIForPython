# 드라이버 다운로드 필수
> Automation이므로 EXE와 통신하는 것이다. 그러므로 드라이버가 필수이다.
- 자신의 브라우저 버전을 채크한다. 
- 해당 버전에 맞는 드라이버를 다운로드 한다(구글이 아닌 [크로니옴 사이트](https://chromedriver.storage.googleapis.com/index.html)에서 받는다). 
- 경로를 설정한다. 

----


Person: 
- python에서 chrome 브라우저를 제어하는 예제를 보여주세요

ChatGPT: 
- Python에서 Chrome 브라우저를 제어하기 위해 "selenium" 라이브러리를 사용할 수 있습니다. Selenium은 웹 애플리케이션 테스트를 자동화하는 도구로, 웹 브라우저를 제어하고 사용자의 동작을 시뮬레이트할 수 있습니다. 다음은 Python에서 Selenium을 사용하여 Chrome 브라우저를 제어하는 간단한 예제입니다.

먼저, `selenium` 패키지를 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다:

```python

pip install selenium
```



다음으로, Selenium이 Chrome 브라우저를 제어하기 위해 Chrome WebDriver를 사용하므로, Chrome WebDriver를 다운로드하여 설치해야 합니다. Chrome WebDriver는 Chrome 브라우저 버전과 호환되는 버전을 선택하여 다운로드해야 합니다. Chrome WebDriver는 다음 링크에서 다운로드할 수 있습니다: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) 

Chrome WebDriver를 다운로드한 후, 다음은 Chrome 브라우저를 열고 웹페이지를 방문하는 간단한 예제입니다:

```python

from selenium import webdriver

# Chrome WebDriver의 경로를 지정합니다.
webdriver_path = 'Chrome WebDriver의 경로'

# Chrome WebDriver를 생성합니다.
driver = webdriver.Chrome(executable_path=webdriver_path)

# Google 홈페이지를 방문합니다.
driver.get('https://www.google.com')

# 브라우저를 닫습니다.
driver.quit()
```



위의 예제에서 `'Chrome WebDriver의 경로'` 부분을 다운로드한 Chrome WebDriver의 실제 경로로 변경해야 합니다. 이제 위의 예제를 실행하면 Chrome 브라우저가 열리고 Google 홈페이지를 방문한 후에 브라우저가 닫힙니다.

이 예제를 확장하여 Chrome 브라우저에서 클릭, 텍스트 입력, 요소 검색 등 다양한 작업을 수행할 수 있습니다. Selenium의 자세한 사용법은 Selenium 공식 문서를 참조하시기 바랍니다.

Person: 
```
1. chrome 드라이버를 소스가 존재하는 경로에 저장했습니다. 
2. www.google.com에 가서 "Vintage appMaker"를 검색합니다. 
3. 결과 화면을 capture.png로 저장합니다. 
소스를 만들어주세요
```

ChatGPT: 
- 아래의 코드는 Python에서 Selenium을 사용하여 Chrome 브라우저를 제어하여 Google 검색을 수행하고 결과 화면을 capture.png로 저장하는 예제입니다.

```python

from selenium import webdriver

# Chrome WebDriver의 경로를 지정합니다.
webdriver_path = 'Chrome WebDriver의 경로'

# Chrome WebDriver를 생성합니다.
driver = webdriver.Chrome(executable_path=webdriver_path)

# Google 홈페이지를 방문합니다.
driver.get('https://www.google.com')

# 검색어를 입력합니다.
search_box = driver.find_element_by_name('q')
search_box.send_keys('Vintage appMaker')

# 검색 버튼을 클릭합니다.
search_button = driver.find_element_by_name('btnK')
search_button.click()

# 결과 화면을 캡처하여 capture.png로 저장합니다.
driver.save_screenshot('capture.png')

# 브라우저를 닫습니다.
driver.quit()
```



위의 코드에서 `'Chrome WebDriver의 경로'` 부분을 다운로드한 Chrome WebDriver의 실제 경로로 변경해야 합니다. 그리고 코드를 실행하면 Chrome 브라우저가 열리고 Google 검색을 수행한 후에 결과 화면이 capture.png로 저장됩니다.

이 코드를 실행하려면 Selenium 패키지가 설치되어 있어야 합니다. 설치되어 있지 않은 경우에는 `pip install selenium` 명령으로 설치할 수 있습니다.

Person: 
- find_element_by_name이 없다고 합니다. 다른 메소드를 사용해야 하나요?

ChatGPT: 
- `find_element_by_name` 메서드는 요소의 `name` 속성을 사용하여 요소를 찾는 메서드입니다. 그러나 Google 검색 버튼은 `name` 속성이 없는 경우도 있을 수 있습니다.

대신에 `find_element_by_xpath` 메서드를 사용하여 요소를 찾을 수 있습니다. XPath는 요소의 위치를 지정하는 경로 언어입니다. 다음은 XPath를 사용하여 검색어 입력란과 검색 버튼을 찾는 예제입니다:

```python

from selenium import webdriver

# Chrome WebDriver의 경로를 지정합니다.
webdriver_path = 'Chrome WebDriver의 경로'

# Chrome WebDriver를 생성합니다.
driver = webdriver.Chrome(executable_path=webdriver_path)

# Google 홈페이지를 방문합니다.
driver.get('https://www.google.com')

# 검색어를 입력합니다.
search_box = driver.find_element_by_xpath('//input[@name="q"]')
search_box.send_keys('Vintage appMaker')

# 검색 버튼을 클릭합니다.
search_button = driver.find_element_by_xpath('//button[@name="btnK"]')
search_button.click()

# 결과 화면을 캡처하여 capture.png로 저장합니다.
driver.save_screenshot('capture.png')

# 브라우저를 닫습니다.
driver.quit()
```



위의 코드에서 XPath 식 `//input[@name="q"]`는 `name` 속성이 "q"인 `<input>` 요소를 찾습니다. `//button[@name="btnK"]`는 `name` 속성이 "btnK"인 `<button>` 요소를 찾습니다. 이렇게 수정된 코드를 실행하면 요소를 정확하게 찾아서 Google 검색을 수행할 수 있습니다.
