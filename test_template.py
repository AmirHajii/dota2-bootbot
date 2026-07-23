import cv2

from config import DEBUG
from game_window import GameWindow
from dx_capture import DXCapture
from template_matcher import TemplateMatcher


def main():

    game = GameWindow()

    if not game.find("Dota 2"):
        print("Dota 2 is not running")
        return

    capture = DXCapture(game)
    matcher = TemplateMatcher()

    template = cv2.imread(
        "templates/item.png",
        cv2.IMREAD_GRAYSCALE
    )

    if template is None:
        print("Template not found")
        return

    while True:

        frame = capture.capture()

        if frame is None:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        result = matcher.find(gray, template)

        if result["found"]:

            print(
                f'Center: {result["center"]} | Confidence: {result["confidence"]:.2f}'
            )

            if DEBUG:

                x, y = result["location"]
                w = result["width"]
                h = result["height"]

                cx, cy = result["center"]

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    frame,
                    (cx, cy),
                    5,
                    (0, 0, 255),
                    -1
                )

                cv2.putText(
                    frame,
                    f'{result["confidence"]:.2f}',
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

        if DEBUG:

            cv2.imshow(
                "Template Detection",
                frame
            )

            if cv2.waitKey(1) == ord("q"):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()