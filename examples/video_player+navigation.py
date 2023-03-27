import cv2 as cv

video_file = '../data/PETS09-S2L1-raw.webm'

# Read the given video file
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given video, ' + video_file

# Get FPS and calculate the waiting time in millisecond
fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)

# Configure the frame navigation
frame_total = int(video.get(cv.CAP_PROP_FRAME_COUNT))
frame_shift = 10
speed_table = [1/10, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 8, 10]
speed_index = 4

while True:
    # Get an image from 'video'
    valid, img = video.read()
    if not valid:
        break

    # Show the image
    frame = int(video.get(cv.CAP_PROP_POS_FRAMES))
    info = f'Frame: {frame}/{frame_total}, Speed: x{speed_table[speed_index]:.2g}'
    cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
    cv.imshow('Video Player', img)

    # Process the key event
    key = cv.waitKey(max(int(wait_msec / speed_table[speed_index]), 1))
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('\t'):
        speed_index = 4
    elif key == ord('>') or key == ord('.'):
        speed_index = min(speed_index + 1, len(speed_table) - 1)
    elif key == ord('<') or key == ord(','):
        speed_index = max(speed_index - 1, 0)
    elif key == ord(']') or key == ord('}'):
        video.set(cv.CAP_PROP_POS_FRAMES, frame + frame_shift)
    elif key == ord('[') or key == ord('{'):
        video.set(cv.CAP_PROP_POS_FRAMES, max(frame - frame_shift, 0))

cv.destroyAllWindows()
