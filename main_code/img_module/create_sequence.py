def create_sequence(cam,masks):
    frame1 = cam.get_frame()
    frame2 = cam.get_frame()
    led_number = len(masks)
    return [[1 for i in range(led_number)],[0 for i in range(led_number)]]