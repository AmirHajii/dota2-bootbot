import cv2

from game_window import GameWindow
from dx_capture import DXCapture


def main():

    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    capture = DXCapture(game)

    while True:

        frame = capture.capture()

        if frame is None:
            continue

        cv2.imshow("DX Capture Test", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()