import time

import win32api
import win32con
import win32gui


class KeyboardController:

    def __init__(self, game_handle=None):
        self.game_handle = game_handle

    def set_game_handle(self, handle):
        self.game_handle = handle

    def _activate_window(self):
        if self.game_handle:
            try:
                win32gui.SetForegroundWindow(self.game_handle)
                time.sleep(0.05)
            except Exception:
                pass

    def _get_vk(self, key):
        mapping = {
            "space": win32con.VK_SPACE,
            "a": ord("A"),
            "d": ord("D"),
        }
        return mapping.get(key, ord(key[0].upper()))

    def _key_down(self, key):
        self._activate_window()
        vk = self._get_vk(key)
        win32api.keybd_event(vk, 0, 0, 0)

    def _key_up(self, key):
        vk = self._get_vk(key)
        win32api.keybd_event(vk, 0, win32con.KEYEVENTF_KEYUP, 0)

    def press_space(self):
        print("SPACE")
        self._key_down("space")
        time.sleep(0.08)
        self._key_up("space")
        time.sleep(0.2)

    def move_left(self):
        print("PRESS A")
        self._key_down("a")
        time.sleep(0.05)
        self._key_up("a")

    def move_right(self):
        print("PRESS D")
        self._key_down("d")
        time.sleep(0.05)
        self._key_up("d")

    def move(self, direction):
        if direction == "LEFT":
            self.move_left()
        elif direction == "RIGHT":
            self.move_right()
