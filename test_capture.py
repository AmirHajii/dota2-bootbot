import cv2

from game_window import GameWindow
from window_capture import WindowCapture


def main():

    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    capture = WindowCapture(game.handle)

    while True:

        image = capture.capture()

        cv2.imshow("Dota 2 Capture", image)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()