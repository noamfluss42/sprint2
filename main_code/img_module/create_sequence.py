import cv2

import time
from main_code.img_module.crop_image import calc_brightness


def get_bit_by_mask(frame, mask, brightness_threshold) -> int:
    print("!!!!!")

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # for i in range(len(mask)):
    #     for j in range(len(mask[i])):
    #         if mask[i][j] == 0:
    #             mask[i][j] = 255
    #         else:
    #             mask[i][j] = 0

    result = cv2.bitwise_and(frame, mask)

    brightness = calc_brightness(result)
    print(brightness)
    print(brightness_threshold)
    if brightness_threshold < brightness:
        return 1
    else:
        return 0


def create_sequence(cam, masks, brightness_thresholds):
    led_number = len(masks)
    # timeout variable can be omitted, if you use specific value in the while condition
    timeout = 20  # [seconds]
    result = []
    timeout_start = time.time()
    while True:
        frame = cam.get_frame()
        result.append([])
        for i in range(led_number):
            result[-1].append(get_bit_by_mask(frame, masks[i],brightness_thresholds[i]))
        print(result)
    return result
