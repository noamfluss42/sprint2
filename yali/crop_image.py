from main_code.receiver import *
import numpy as np


class CropImage:

    WINDOW_NAME = f"{ARAZY}"
    MASK = 'mask'
    R = 3
    mask = np.zeros((480, 640), np.uint8)

    def __init__(self):
        self.frame = None

    def run(self):
        cam = Camera(ARAZY)
        cv2.namedWindow(self.WINDOW_NAME)
        cv2.namedWindow(self.MASK)
        cv2.setMouseCallback(self.WINDOW_NAME, self.click)

        while True:
            f = cv2.imread(r'Screenshot 2020-12-29 145155.png')
            self.frame = f[-480:, :640]  #cam.get_frame()

            # Display the resulting frame
            cv2.imshow(self.WINDOW_NAME, self.frame)
            cv2.imshow(self.MASK, self.mask)

            key = cv2.waitKey(1)
            if key == 13:  # 13 is the Enter Key
                break

        cv2.destroyAllWindows()
        cam.end()

    def click(self, event, x, y, *args):
        # check to see if the left mouse button was released
        if event == cv2.EVENT_LBUTTONUP:
            self.crop(x, y, True)

        # check to see if the left mouse button was released
        elif event == cv2.EVENT_RBUTTONUP:
            self.crop(x, y, False)

    def crop(self, x, y, crop):
        r = self.R if crop else int(1.5*self.R)
        self.mask[y-r:y+r, x-r:x+r] = 255 if crop else 0


if __name__ == '__main__':
    c = CropImage()
    c.run()
