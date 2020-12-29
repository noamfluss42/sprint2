import numpy as np
import cv2
from main_code.img_module.crop_image import *
from main_code.img_module.create_sequence import *


def calc_brightness(image: np.ndarray) -> float:
    return np.average(image)


def main():
    # video feed
    cam = Camera(ARAZY)
    recognizer = RecognizeLed(cam)
    recognizer.run()

    create_sequence(cam, recognizer.masks)



if __name__ == '__main__':
    main()
