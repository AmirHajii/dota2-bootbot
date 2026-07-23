import pyautogui
import time


class KeyboardController:

    def __init__(self):
        pass


    def press_space(self):

        pyautogui.keyDown("space")
        time.sleep(0.05)
        pyautogui.keyUp("space")


    def move_left(self):

        pyautogui.keyDown("d")
        time.sleep(0.05)
        pyautogui.keyUp("d")


    def move_right(self):

        pyautogui.keyDown("a")
        time.sleep(0.05)
        pyautogui.keyUp("a")


    def move(
        self,
        direction
    ):

        if direction == "LEFT":

            self.move_left()


        elif direction == "RIGHT":

            self.move_right()