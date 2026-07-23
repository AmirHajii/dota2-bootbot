import cv2

from config import MATCH_THRESHOLD


class TemplateMatcher:

    def __init__(self):
        self.threshold = MATCH_THRESHOLD

    def find(self, image, template, threshold=None):

        if threshold is None:
            threshold = self.threshold

        result = cv2.matchTemplate(
            image,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        _, max_value, _, max_location = cv2.minMaxLoc(result)

        h, w = template.shape[:2]

        x = max_location[0]
        y = max_location[1]

        return {
            "confidence": max_value,
            "location": (x, y),
            "center": (x + w // 2, y + h // 2),
            "width": w,
            "height": h,
            "found": max_value >= threshold
        }
