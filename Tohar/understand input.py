from bitarray import bitarray



def frames_to_data(list_of_frames):
    last_frame = list_of_frames[0]# first frame
    all_data = []
    all_data += last_frame[:-1]
    for frame in list_of_frames:
        frame_data = frame[:-1]
        control = frame[-1]
        if is_new_frame(frame, last_frame):
            all_data += frame_data
            last_frame = frame
        else:
            print("old frame")

        print(frame_data, control)
    return all_data

def is_new_frame(new_frame, old_frame):
    new_control = new_frame[-1]
    old_control = old_frame[-1]
    if new_control == old_control:
        return False
    return True


if __name__ == '__main__':
    frames = [[0,1,1,0,1], [0,1,1,0,1], [1,0,1,0,0], [0,0,0,0,1]]
    data = frames_to_data(frames)
    print("data:\n", data)
