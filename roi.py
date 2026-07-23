class ROI:

    def __init__(self):
        pass

    def crop(self, image, x, y, width, height):

        roi = image[
            y:y + height,
            x:x + width
        ]

        return roi