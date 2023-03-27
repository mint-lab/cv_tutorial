import cv2 as cv

video_file = '../data/PETS09-S2L1-raw.webm'

# Read the given video file
# Note) Additional argument examples
# - Image sequence: video_file = '../data/PETS09-S2L1-raw_%04d.png'
# - Camera        : video_file = 0 (Note: The camera index)
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given video, ' + video_file

# Get FPS and calculate the waiting time in millisecond
fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)

while True:
    # Read an image from 'video'
    valid, img = video.read()
    if not valid:
        break

    # Show the image
    cv.imshow('Video Player', img)

    # Terminate if the given key is ESC
    key = cv.waitKey(wait_msec)
    if key == 27: # ESC
        break

cv.destroyAllWindows()
