import numpy as np
import cv2
from main_code.img_module.crop_image import *
from main_code.img_module.create_sequence import *




def main():
    # video feed
    cam = Camera(ARAZY)
    recognizer = RecognizeLed(cam)
    recognizer.run()

    print(create_sequence(cam, recognizer.masks, recognizer.get_threshold()))


if __name__ == '__main__':
    main()
