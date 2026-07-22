import cv2

from game_window import GameWindow
from game_capture import GameCapture


game = GameWindow()

if not game.find():
    print("Dota 2 is not running")
    exit()

capture = GameCapture(game)

while True:

    image = capture.capture()

    cv2.imshow("Dota 2", image)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()