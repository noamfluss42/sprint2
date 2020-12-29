from main_code.receiver import *

import time


def main():
    cam = Camera(DANIEL)

    # print("Camera is alive?: " + str(cam.p.is_alive()))
    # timeout variable can be omitted, if you use specific value in the while condition
    count = 0

    timeout = 20  # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        frame = cam.get_frame()
        count += 1
    print(count)

    cv2.destroyAllWindows()

    cam.end()


if __name__ == '__main__':
    for i in range(10):
        main()
        time.sleep(5)
