import pyautogui
import time

# 3초 대기 후 메모장을 실행하고 입력을 시작합니다.
time.sleep(3)
pyautogui.press('winleft')
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)

# 메모장 창을 찾습니다.
window_title = "제목 없음"  # 찾으려는 윈도우의 제목
notepad_window = None
for window in pyautogui.getAllWindows():
    if window_title in window.title:
        notepad_window = window
        break

# 메모장 창이 찾아지지 않은 경우 오류 메시지를 출력하고 프로그램을 종료합니다.
if not notepad_window:
    print(f"메모장 창을 찾을 수 없습니다: {window_title}")
    pyautogui.hotkey('alt', 'f4')
    exit()

# 윈도우 창의 위치와 크기를 가져옵니다.
window_x = notepad_window.left
window_y = notepad_window.top
window_width = notepad_window.width
window_height = notepad_window.height

print(f"창 위치: ({window_x}, {window_y})")
print(f"창 크기: {window_width} x {window_height}")

# 프로그램을 종료합니다.
pyautogui.hotkey('alt', 'f4')