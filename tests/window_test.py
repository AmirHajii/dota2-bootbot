import pygetwindow as gw

windows = gw.getWindowsWithTitle("Dota 2")

if not windows:
    print("Dota 2 is not running")

else:
    window = windows[0]

    print("Dota 2 found")
    print("Title :", window.title)
    print("Left :", window.left)
    print("Top :", window.top)
    print("Width :", window.width)
    print("Height :", window.height)