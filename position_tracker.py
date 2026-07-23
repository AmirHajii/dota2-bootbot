class PositionTracker:

    def __init__(self):
        pass


    def get_direction(
        self,
        cart_position,
        shoe_position
    ):

        cart_x = cart_position[0]
        shoe_x = shoe_position[0]


        distance = shoe_x - cart_x


        if distance < -20:

            return "LEFT"


        elif distance > 20:

            return "RIGHT"


        else:

            return "STOP"