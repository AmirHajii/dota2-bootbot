import dxcam


class DXCapture:

    def __init__(self, game_window):
        self.game_window = game_window
        self.camera = dxcam.create()

    def capture(self):
        region = (
            self.game_window.left,
            self.game_window.top,
            self.game_window.left + self.game_window.width,
            self.game_window.top + self.game_window.height
        )
        try:
            frame = self.camera.grab(region=region)
            return frame
        except ValueError:
            return None
