from game_state import GameState


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


    def find_object(
        self,
        image,
        template
    ):

        result = self.matcher.find(
            image,
            template
        )

        if result["found"]:

            return result["center"]


        return None


    def update(
        self,
        image,
        space_ready_template,
        aiming_template,
        cart_template,
        shoe_template
    ):

        state = self.game_manager.get_state()


        # شروع مرحله
        if state == GameState.WAIT_FOR_NEW_LEVEL:


            if self.state_detector.detect_space_ready(
                image,
                space_ready_template
            ):

                self.keyboard.press_space()

                self.game_manager.set_state(
                    GameState.AIMING
                )


        # نشانه گیری
        elif state == GameState.AIMING:


            if self.state_detector.detect_aiming(
                image,
                aiming_template
            ):

                self.keyboard.press_space()

                self.game_manager.set_state(
                    GameState.THROWING
                )


        # دنبال کردن کفش
        elif state == GameState.THROWING:


            cart_position = self.find_object(
                image,
                cart_template
            )


            shoe_position = self.find_object(
                image,
                shoe_template
            )


            if cart_position and shoe_position:


                direction = self.position_tracker.get_direction(
                    cart_position,
                    shoe_position
                )


                print(
                    "Direction:",
                    direction
                )


                self.keyboard.move(
                    direction
                )


        return self.game_manager.get_state()