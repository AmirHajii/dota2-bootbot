import pyautogui
import time


class KeyboardController:

    def __init__(self):
        pass

    def press_left(self):
        pyautogui.keyDown("d")
        time.sleep(0.1)
        pyautogui.keyUp("d")

    def press_right(self):
        pyautogui.keyDown("a")
        time.sleep(0.1)
        pyautogui.keyUp("a")