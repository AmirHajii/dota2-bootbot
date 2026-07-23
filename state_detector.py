import cv2


class StateDetector:

    def __init__(self, matcher):
        self.matcher = matcher


    def detect_space_ready(self, image, template):

        result = self.matcher.find(
            image,
            template
        )

        return result["found"]