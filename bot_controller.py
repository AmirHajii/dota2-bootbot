from game_state import GameState
from trajectory_predictor import TrajectoryPredictor
import time


class BotController:

    def __init__(
        self,
        game_manager,
        state_detector,
        keyboard,
        matcher,
        position_tracker
    ):

        self.game_manager = game_manager
        self.state_detector = state_detector
        self.keyboard = keyboard
        self.matcher = matcher
        self.position_tracker = position_tracker

        self.game_over_start_time = None

        self.last_direction = "STOP"

        # NEW
        self.predictor = TrajectoryPredictor()


    def update(
        self,
        image,
        space_ready_template,
        aiming_template,
        cart_template,
        shoe_template,
        game_over_template=None,
        pause_template=None
    ):

        state = self.game_manager.get_state()

        if pause_template is not None:

            paused = self.state_detector.detect_pause(
                image,
                pause_template
            )

            if paused:

                if state != GameState.PAUSED:

                    self.game_manager.set_state(
                        GameState.PAUSED
                    )

                    print("PAUSED")

                return state


            if state == GameState.PAUSED:

                self.game_manager.set_state(
                    GameState.WAIT_FOR_NEW_LEVEL
                )

                print("RESUME")

                state = GameState.WAIT_FOR_NEW_LEVEL



        if state == GameState.WAIT_FOR_NEW_LEVEL:


            if self.state_detector.detect_space_ready(
                image,
                space_ready_template
            ):

                print("SPACE 1 - START")

                self.keyboard.press_space()

                self.game_manager.set_state(
                    GameState.AIMING
                )



        elif state == GameState.AIMING:


            if self.state_detector.detect_aiming(
                image,
                aiming_template
            ):

                print("SPACE 2 - THROW")

                self.keyboard.press_space()

                self.game_manager.set_state(
                    GameState.THROWING
                )



        elif state == GameState.THROWING:


            if (
                game_over_template is not None
                and
                self.state_detector.detect_game_over(
                    image,
                    game_over_template
                )
            ):

                print("GAME OVER")

                self.game_manager.set_state(
                    GameState.GAME_OVER
                )

                self.game_over_start_time = time.time()

            else:

                self._track_and_position(
                    image,
                    shoe_template,
                    cart_template,
                    space_ready_template
                )



        elif state == GameState.GAME_OVER:


            waiting = False

            if self.game_over_start_time:

                waiting = (
                    time.time()
                    -
                    self.game_over_start_time
                    >
                    2.0
                )


            if (
                waiting
                and
                self.state_detector.detect_space_ready(
                    image,
                    space_ready_template
                )
            ):

                print("RESTART")

                self.keyboard.press_space()

                self.game_manager.set_state(
                    GameState.AIMING
                )

                self.game_over_start_time = None



        return self.game_manager.get_state()



    def _track_and_position(
        self,
        image,
        shoe_template,
        cart_template,
        space_ready_template
    ):


        if self.state_detector.detect_space_ready(
            image,
            space_ready_template
        ):

            print("CAUGHT - NEXT LEVEL")

            self.predictor.clear()

            self.keyboard.press_space()

            self.game_manager.set_state(
                GameState.AIMING
            )

            self.last_direction = "STOP"

            return



        cart_result = self.state_detector.detect_cart(
            image,
            cart_template
        )


        shoe_result = self.state_detector.detect_shoe(
            image,
            shoe_template
        )


        if cart_result["found"]:

            if shoe_result["found"]:

                self.predictor.update(
                    shoe_result["center"]
                )

                target = self.predictor.predict()

                if target is None:
                    target = shoe_result["center"]

                direction = self.position_tracker.get_direction(
                    cart_result["center"],
                    target
                )

                if direction != self.last_direction:

                    print(
                        "Predicted:", target,
                        "Direction:", direction
                    )

                    self.keyboard.move(direction)

                    self.last_direction = direction


            else:

                print(
                    f"Cart found ({cart_result['confidence']:.2f}) but Shoe NOT found"
                )

                if self.last_direction != "STOP":

                    self.keyboard.move("STOP")

                    self.last_direction = "STOP"


        else:

            print(
                f"Cart NOT found | "
                f"Shoe: {'OK' if shoe_result['found'] else 'NO'} "
                f"(cart conf: {cart_result['confidence']:.2f}, "
                f"shoe conf: {shoe_result['confidence']:.2f})"
            )

            if self.last_direction != "STOP":

                self.keyboard.move("STOP")

                self.last_direction = "STOP"