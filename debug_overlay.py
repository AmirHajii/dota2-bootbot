import cv2


class DebugOverlay:

    def __init__(self):
        pass


    def draw_match(
        self,
        frame,
        result,
        color,
        label
    ):

        if not result["found"]:

            cv2.putText(
                frame,
                f"{label}: NOT FOUND",
                (20, 30 if label == "Cart" else 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

            return


        x, y = result["location"]

        h = result["height"]
        w = result["width"]


        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            color,
            2
        )


        cx, cy = result["center"]


        cv2.circle(
            frame,
            (cx, cy),
            4,
            color,
            -1
        )


        confidence = result["confidence"]


        cv2.putText(
            frame,
            f"{label}: {confidence:.2f}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )