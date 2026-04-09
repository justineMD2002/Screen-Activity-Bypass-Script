import pyautogui
import random
import time

pyautogui.FAILSAFE = True  # move mouse to top-left corner to stop

screen_w, screen_h = pyautogui.size()

def random_move():
    x = random.randint(100, screen_w - 100)
    y = random.randint(100, screen_h - 100)
    duration = random.uniform(0.1, 0.3)
    pyautogui.moveTo(x, y, duration=duration)

def random_scroll():
    x = random.randint(100, screen_w - 100)
    y = random.randint(100, screen_h - 100)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.25))
    scroll_amount = random.choice([*range(-10, -2), *range(3, 11)])
    pyautogui.scroll(scroll_amount)

# def random_click():
#     x = random.randint(100, screen_w - 100)
#     y = random.randint(100, screen_h - 100)
#     pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.25))
#     pyautogui.click()

def alt_tab():
    pyautogui.hotkey('alt', 'tab')

def alt_tab_multi():
    # Hold alt, press tab multiple times to cycle forward through windows
    tabs = random.randint(2, 4)
    pyautogui.keyDown('alt')
    for _ in range(tabs):
        pyautogui.press('tab')
        time.sleep(random.uniform(0.15, 0.4))
    pyautogui.keyUp('alt')

def alt_shift_tab():
    # Hold alt, press shift+tab to cycle backward
    pyautogui.keyDown('alt')
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('alt')

def alt_tab_then_back():
    # Go forward a few tabs, then back one with shift+tab
    tabs_forward = random.randint(2, 3)
    pyautogui.keyDown('alt')
    for _ in range(tabs_forward):
        pyautogui.press('tab')
        time.sleep(random.uniform(0.15, 0.35))
    # go back one
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')
    time.sleep(random.uniform(0.15, 0.3))
    pyautogui.keyUp('alt')

def ctrl_tab():
    pyautogui.hotkey('ctrl', 'tab')

def ctrl_tab_multi():
    # Ctrl+tab multiple times for browser/editor tab cycling
    tabs = random.randint(2, 4)
    for _ in range(tabs):
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(random.uniform(0.2, 0.5))

def ctrl_shift_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

actions = [
    random_move, random_move,
    random_scroll, random_scroll,
    alt_tab, alt_tab_multi, alt_shift_tab, alt_tab_then_back,
    ctrl_tab, ctrl_tab_multi, ctrl_shift_tab,
]

print("[activity] started — move mouse to TOP-LEFT corner to stop")

while True:
    action = random.choice(actions)
    action()
    delay = random.uniform(4, 7)
    time.sleep(delay)
