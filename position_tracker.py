class PositionTracker:

    def __init__(self):

        self.dead_zone = 20

        self.fast_zone = 250

        self.medium_zone = 120



    def get_direction(
        self,
        cart_position,
        shoe_position
    ):

        cart_x = cart_position[0]
        shoe_x = shoe_position[0]

        distance = shoe_x - cart_x


        if abs(distance) <= self.dead_zone:

            return "STOP"


        if distance < 0:

            if abs(distance) > self.fast_zone:

                return "LEFT_FAST"

            elif abs(distance) > self.medium_zone:

                return "LEFT"

            else:

                return "LEFT_SLOW"


        else:

            if abs(distance) > self.fast_zone:

                return "RIGHT_FAST"

            elif abs(distance) > self.medium_zone:

                return "RIGHT"

            else:

                return "RIGHT_SLOW"