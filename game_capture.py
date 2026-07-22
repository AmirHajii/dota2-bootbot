from mss import MSS
import numpy as np


class GameCapture:

    def __init__(self, game_window):
        self.game_window = game_window
        self.sct = MSS()

    def capture(self):
        monitor = {
            "left": self.game_window.left,
            "top": self.game_window.top,
            "width": self.game_window.width,
            "height": self.game_window.height,
        }

        screenshot = self.sct.grab(monitor)

        image = np.array(screenshot)

        return image