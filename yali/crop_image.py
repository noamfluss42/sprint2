from main_code.receiver import *
import numpy as np


class CropImage:

    WINDOW_NAME = f"{ARAZY}"
    MASK = 'mask'

    def __init__(self):
        self.x = None
        self.y = None
        self.mask = np.zeros((480, 640), np.uint8)
        self.cropping = False

    def run(self):
        cam = Camera(ARAZY)
        cv2.namedWindow(self.WINDOW_NAME)
        cv2.namedWindow(self.MASK)
        cv2.setMouseCallback(self.WINDOW_NAME, self.click_and_crop)

        while True:
            self.frame = cam.get_frame()

            # Display the resulting frame
            cv2.imshow(self.WINDOW_NAME, self.frame)
            cv2.imshow(self.MASK, self.mask)

            key = cv2.waitKey(1)
            if key == 13:  # 13 is the Enter Key
                break

        cv2.destroyAllWindows()
        cam.end()

    def get_mouse_location(self, event, x, y, flags, param):
        self.x, self.y = x, y

    def click_and_crop(self, event, x, y, flags, param):
        # grab references to the global variables
        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being
        # performed
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x, self.y = x, y
            self.cropping = True
        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            self.crop(self.x, x, self.y, y)
            self.cropping = False

        elif event == cv2.EVENT_RBUTTONDOWN:
            self.x, self.y = x, y
            self.cropping = True
        # check to see if the left mouse button was released
        elif event == cv2.EVENT_RBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            self.crop(self.x, x, self.y, y)
            self.cropping = False

    def crop(self, x1, x2, y1, y2):
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        start_y = min(y1, y2)
        end_y = max(y1, y2)

        self.mask[start_y:end_y, start_x:end_x] = 255 if self.cropping else 0


if __name__ == '__main__':
    c = CropImage()
    c.run()
