import cv2

from config import MATCH_THRESHOLD


class TemplateMatcher:

    def __init__(self):
        pass

    def find(self, image, template):

        result = cv2.matchTemplate(
            image,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        _, max_value, _, max_location = cv2.minMaxLoc(result)

        template_height, template_width = template.shape

        x = max_location[0]
        y = max_location[1]

        center_x = x + template_width // 2
        center_y = y + template_height // 2

        return {
            "confidence": max_value,
            "location": (x, y),
            "center": (center_x, center_y),
            "width": template_width,
            "height": template_height,
            "found": max_value >= MATCH_THRESHOLD
        }