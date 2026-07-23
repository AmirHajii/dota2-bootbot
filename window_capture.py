import win32gui
import win32ui
import win32con
import numpy as np


class WindowCapture:

    def __init__(self, hwnd):
        self.hwnd = hwnd

    def capture(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)

        width = right - left
        height = bottom - top

        window_dc = win32gui.GetWindowDC(self.hwnd)

        dc_obj = win32ui.CreateDCFromHandle(window_dc)
        compatible_dc = dc_obj.CreateCompatibleDC()

        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(dc_obj, width, height)

        compatible_dc.SelectObject(bitmap)

        compatible_dc.BitBlt(
            (0, 0),
            (width, height),
            dc_obj,
            (0, 0),
            win32con.SRCCOPY
        )

        bitmap_info = bitmap.GetBitmapBits(True)

        image = np.frombuffer(
            bitmap_info,
            dtype=np.uint8
        )

        image = image.reshape(
            height,
            width,
            4
        )

        dc_obj.DeleteDC()
        compatible_dc.DeleteDC()
        win32gui.ReleaseDC(
            self.hwnd,
            window_dc
        )
        win32gui.DeleteObject(
            bitmap.GetHandle()
        )

        return image