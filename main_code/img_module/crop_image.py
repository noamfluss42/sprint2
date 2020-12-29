from main_code.img_module.main import calc_brightness
from main_code.receiver import *
import numpy as np


class RecognizeLed:
    WINDOW_NAME = f"{ARAZY}"
    MASK = 'mask'
    R = 6
    masks = []
    bright_values = []
    dark_values = []
    leds_counter = -1

    def __init__(self, cam):
        self.cam = cam
        self.frame = None

    def run(self):
        cv2.namedWindow(self.WINDOW_NAME)
        cv2.setMouseCallback(self.WINDOW_NAME, self.click)

        while True:
            self.frame = self.cam.get_frame()

            # Display the resulting frame
            cv2.imshow(self.WINDOW_NAME, self.frame)
            self.show_cropped()

            key = cv2.waitKey(1)
            if key == 13:  # 13 is the Enter Key
                break

        cv2.destroyAllWindows()

    def click(self, event, x, y, *args):
        # check to see if the left mouse button was released
        if event == cv2.EVENT_LBUTTONUP:
            self.crop(x, y)

        # check to see if the left mouse button was released
        elif event == cv2.EVENT_RBUTTONUP:
            self.crop(x, y, True)

    def crop(self, x, y, leds_off=False):
        self.leds_counter += 1
        r = self.R
        self.brightness_values(self.frame[y-r:y+r, x-r:x+r], leds_off)

        mask = np.zeros((480, 640), np.uint8)
        mask[y-r:y+r, x-r:x+r] = 255
        self.masks.append(mask)

    def brightness_values(self, cropped, leds_off):
        brightness = calc_brightness(cropped)
        if leds_off:
            self.dark_values.append(brightness)
        else:
            self.bright_values.append(brightness)

    def show_cropped(self):
        gray_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        return [cv2.imshow(f"{self.MASK}{self.leds_counter}", cv2.bitwise_and(gray_frame, mask)) for mask in self.masks]

    def get_masks(self):
        return self.masks


class FakeCamera:
    def __init__(self, *args):
        pass

    def get_frame(self):
        f = cv2.imread(r'Screenshot 2020-12-29 145155.png')
        return f[-480:, :640]

    def end(self):
        pass


if __name__ == '__main__':
    c = RecognizeLed(None)
    c.run()
    masks = c.get_masks()
    for mask_index in range(len(masks)):
        cv2.imwrite("mask" + str(mask_index) + ".png", masks[mask_index])
