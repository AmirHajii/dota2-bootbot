import pygetwindow as gw


class GameWindow:

    def __init__(self):
        self.title = None
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0

    def find(self, title):
        windows = gw.getWindowsWithTitle(title)

        if not windows:
            return False

        window = windows[0]

        self.title = window.title
        self.left = window.left
        self.top = window.top
        self.width = window.width
        self.height = window.height

        return True