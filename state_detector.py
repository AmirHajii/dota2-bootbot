class StateDetector:

    def __init__(self, matcher):
        self.matcher = matcher

    def _find(self, image, template):
        if template is None:
            return {"found": False, "location": (0, 0), "center": (0, 0)}
        return self.matcher.find(image, template)

    def detect_space_ready(self, image, template):
        return self._find(image, template)["found"]

    def detect_aiming(self, image, template):
        return self._find(image, template)["found"]

    def detect_cart(self, image, template):
        return self._find(image, template)

    def detect_shoe(self, image, template):
        return self._find(image, template)

    def detect_game_over(self, image, template):
        return self._find(image, template)["found"]

    def detect_pause(self, image, template):
        return self._find(image, template)["found"]