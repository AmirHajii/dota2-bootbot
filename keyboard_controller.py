import time

import win32api
import win32con
import win32gui


class KeyboardController:

    def __init__(self, game_handle=None):

        self.game_handle = game_handle

        self.left_pressed = False
        self.right_pressed = False


    def set_game_handle(self, handle):

        self.game_handle = handle


    def _activate_window(self):

        if self.game_handle:

            try:

                win32gui.SetForegroundWindow(
                    self.game_handle
                )

                time.sleep(0.05)

            except Exception:

                pass


    def _get_vk(self, key):

        mapping = {
            "space": win32con.VK_SPACE,
            "a": ord("A"),
            "d": ord("D"),
        }

        return mapping.get(
            key,
            ord(key[0].upper())
        )


    def _key_down(self, key):

        self._activate_window()

        vk = self._get_vk(key)

        win32api.keybd_event(
            vk,
            0,
            0,
            0
        )


    def _key_up(self, key):

        vk = self._get_vk(key)

        win32api.keybd_event(
            vk,
            0,
            win32con.KEYEVENTF_KEYUP,
            0
        )


    def press_space(self):

        print("SPACE")

        self._key_down("space")

        time.sleep(0.08)

        self._key_up("space")

        time.sleep(0.2)


    def _hold_left(self):

        if not self.left_pressed:

            self._key_down("a")

            self.left_pressed = True


    def _release_left(self):

        if self.left_pressed:

            self._key_up("a")

            self.left_pressed = False


    def _hold_right(self):

        if not self.right_pressed:

            self._key_down("d")

            self.right_pressed = True


    def _release_right(self):

        if self.right_pressed:

            self._key_up("d")

            self.right_pressed = False


    def move(self, direction):

        if direction == "STOP":

            self._release_left()
            self._release_right()

            return


        if direction == "LEFT_FAST":

            self._release_right()

            self._hold_left()

            return


        if direction == "LEFT":

            self._release_right()

            self._hold_left()

            return


        if direction == "LEFT_SLOW":

            self._release_right()

            self._key_down("a")

            time.sleep(0.02)

            self._key_up("a")

            return


        if direction == "RIGHT_FAST":

            self._release_left()

            self._hold_right()

            return


        if direction == "RIGHT":

            self._release_left()

            self._hold_right()

            return


        if direction == "RIGHT_SLOW":

            self._release_left()

            self._key_down("d")

            time.sleep(0.02)

            self._key_up("d")

            return