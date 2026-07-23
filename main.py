import cv2

from config import DEBUG

from game_window import GameWindow
from dx_capture import DXCapture

from template_matcher import TemplateMatcher
from state_detector import StateDetector

from game_manager import GameManager
from keyboard_controller import KeyboardController
from position_tracker import PositionTracker
from trajectory_predictor import TrajectoryPredictor

from bot_controller import BotController
from debug_overlay import DebugOverlay


def load_template(path):

    template = cv2.imread(
        path,
        cv2.IMREAD_GRAYSCALE
    )

    if template is None:

        raise Exception(
            f"Template not found: {path}"
        )

    return template


def main():

    game = GameWindow()

    if not game.find("Dota 2"):

        print("Dota 2 not found")
        return


    capture = DXCapture(game)

    matcher = TemplateMatcher()

    detector = StateDetector(
        matcher
    )

    manager = GameManager()

    keyboard = KeyboardController(
        game.handle
    )

    tracker = PositionTracker()

    predictor = TrajectoryPredictor()

    overlay = DebugOverlay()

    bot = BotController(
        manager,
        detector,
        keyboard,
        matcher,
        tracker
    )


    space_ready = load_template(
        "templates/space_ready.png"
    )

    aiming = load_template(
        "templates/aiming.png"
    )

    cart = load_template(
        "templates/cart.png"
    )

    shoe = load_template(
        "templates/shoe.png"
    )

    while True:

        frame = capture.capture()

        if frame is None:
            continue

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # ---------- DEBUG ----------
        cart_result = detector.detect_cart(
            gray,
            cart
        )

        shoe_result = detector.detect_shoe(
            gray,
            shoe
        )

        overlay.draw_match(
            frame,
            cart_result,
            (0, 255, 0),
            "Cart"
        )

        overlay.draw_match(
            frame,
            shoe_result,
            (0, 0, 255),
            "Shoe"
        )
        # ---------------------------

        state = bot.update(
            gray,
            space_ready,
            aiming,
            cart,
            shoe
        )

        print(
            "Current State:",
            state
        )

        if DEBUG:

            cv2.imshow(
                "Bot Debug",
                frame
            )

            if cv2.waitKey(1) == ord("q"):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()