import cv2

import time
from main_code.img_module.main import calc_brightness


def get_bit_by_mask(frame, mask, brightness_threshold) -> int:
    result = cv2.bitwise_and(frame, mask)
    brightness = calc_brightness(result)
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
    while time.time() < timeout_start + timeout:
        frame = cam.get_frame()
        result.append([])
        for i in range(led_number):
            result[-1].append(get_bit_by_mask(frame, masks[i],brightness_thresholds[i]))
    return result
