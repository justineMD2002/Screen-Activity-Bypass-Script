import pyautogui
import random
import time

pyautogui.FAILSAFE = True  # move mouse to top-left corner to stop

screen_w, screen_h = pyautogui.size()

def random_move():
    x = random.randint(100, screen_w - 100)
    y = random.randint(100, screen_h - 100)
    duration = random.uniform(0.2, 1.5)
    pyautogui.moveTo(x, y, duration=duration)

def random_scroll():
    x = random.randint(100, screen_w - 100)
    y = random.randint(100, screen_h - 100)
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.5))
    scroll_amount = random.randint(-5, 5)
    pyautogui.scroll(scroll_amount)

def random_click():
    x = random.randint(100, screen_w - 100)
    y = random.randint(100, screen_h - 100)
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.7))
    pyautogui.click()

actions = [random_move, random_move, random_scroll, random_scroll, random_click]

print("[activity] started — move mouse to TOP-LEFT corner to stop")

while True:
    action = random.choice(actions)
    action()
    delay = random.uniform(3, 12)
    time.sleep(delay)
