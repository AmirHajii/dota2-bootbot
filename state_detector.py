from config import MATCH_THRESHOLD, SPACE_READY_THRESHOLD, AIMING_THRESHOLD, SHOE_THRESHOLD


class StateDetector:

    def __init__(self, matcher):
        self.matcher = matcher

    def _find(self, image, template, threshold=None):
        if template is None:
            return {"found": False, "location": (0, 0), "center": (0, 0)}
        return self.matcher.find(image, template, threshold)

    def detect_space_ready(self, image, template):
        return self._find(image, template, SPACE_READY_THRESHOLD)["found"]

    def detect_aiming(self, image, template):
        return self._find(image, template, AIMING_THRESHOLD)["found"]

    def detect_cart(self, image, template):
        return self._find(image, template, MATCH_THRESHOLD)

    def detect_shoe(self, image, template):
        return self._find(image, template, SHOE_THRESHOLD)

    def detect_game_over(self, image, template):
        return self._find(image, template)["found"]

    def detect_pause(self, image, template):
        return self._find(image, template)["found"]