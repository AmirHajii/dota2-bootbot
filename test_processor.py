import cv2

from game_window import GameWindow
from dx_capture import DXCapture
from image_processor import ImageProcessor
from roi import ROI


def main():

    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    capture = DXCapture(game)
    processor = ImageProcessor()
    roi = ROI()

    while True:

        frame = capture.capture()

        if frame is None:
            continue

        gray = processor.to_gray(frame)

        cropped = roi.crop(
            gray,
            800,
            300,
            500,
            500
        )

        cv2.imshow("Original", frame)
        cv2.imshow("Gray", gray)
        cv2.imshow("ROI", cropped)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()