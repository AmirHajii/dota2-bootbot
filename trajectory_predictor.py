from collections import deque


class TrajectoryPredictor:

    def __init__(self):

        self.history = deque(maxlen=5)


    def update(self, position):

        self.history.append(position)


    def clear(self):

        self.history.clear()


    def can_predict(self):

        return len(self.history) >= 2


    def velocity(self):

        if not self.can_predict():

            return (0, 0)

        count = len(self.history)
        vx_total = 0
        vy_total = 0

        for i in range(1, count):
            x1, y1 = self.history[i - 1]
            x2, y2 = self.history[i]
            vx_total += x2 - x1
            vy_total += y2 - y1

        return (
            vx_total // count,
            vy_total // count
        )


    def predict(self):

        if not self.can_predict():

            return None

        vx, vy = self.velocity()

        x, y = self.history[-1]

        if abs(vx) > 500 or abs(vy) > 500:
            return None

        return (
            x + vx,
            y + vy
        )