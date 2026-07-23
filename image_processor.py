import cv2


class ImageProcessor:

    def __init__(self):
        pass

    def to_gray(self, image):
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        return gray