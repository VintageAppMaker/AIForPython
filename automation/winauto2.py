import pyautogui
import time

# 개발자 매뉴얼을 참고한 심플한 예제
# https://pyautogui.readthedocs.io/en/latest/index.html?highlight=click
def FindAndClick(seconds):
    time.sleep(seconds)
    # 윈도우 화면에서 원하는 곳을 캡쳐함
    lst = pyautogui.locateAllOnScreen('click.png')
    print("click.png => 찾기" )
        
    # 찾았다면 배열 중에서 첫번째만 클릭
    for i in lst:
        print(str(i) + " -> 클릭함" )
        pyautogui.click(i.left + 15, i.top + 15)
        break
        

# 무한대기, 2초 반복
while True:    
    FindAndClick(2)    
