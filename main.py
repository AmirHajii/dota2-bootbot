from game_window import GameWindow
from game_capture import GameCapture
from image_processor import ImageProcessor


def main():
    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    print("Dota 2 found")
    print(f"Title: {game.title}")
    print(f"Left: {game.left}")
    print(f"Top: {game.top}")
    print(f"Width: {game.width}")
    print(f"Height: {game.height}")

    capture = GameCapture(game)
    processor = ImageProcessor()

    image = capture.capture()

    roi = processor.crop(image, 0, 0, 500, 500)

    print(type(image))
    print(type(roi))


if __name__ == "__main__":
    main()