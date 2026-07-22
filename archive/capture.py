from mss import MSS
import cv2
import numpy as np

with MSS() as sct:
    monitor = sct.monitors[1]

    while True:
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)

        cv2.imshow("BootBot", img)

        if cv2.waitKey(1) == ord("q"):
            break

cv2.destroyAllWindows()