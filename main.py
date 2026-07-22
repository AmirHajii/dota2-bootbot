import cv2

from game_window import GameWindow
from game_capture import GameCapture
from image_processor import ImageProcessor


def main():
    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    capture = GameCapture(game)
    processor = ImageProcessor()

    image = capture.capture()

    roi = processor.crop(image, 0, 0, 500, 500)

    cv2.imshow("Game", image)
    cv2.imshow("ROI", roi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()