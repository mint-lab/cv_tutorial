import numpy as np
import cv2 as cv

# Read the given video
video = cv.VideoCapture('../data/PETS09-S2L1-raw.webm')
assert video.isOpened(), 'Cannot read the given video'

frame_count = 0
img_back = None
while True:
    # Get an image from 'video'
    valid, img = video.read()
    if not valid:
        break
    frame_count += 1

    # Show progress
    if frame_count % 100 == 0:
        print(f'Frame: {frame_count}')

    # Add the image to the averaged image (the background image)
    # Alternative) cv.createBackgroundSubtractorMOG2(), cv::bgsegm
    if img_back is None:
        img_back = np.zeros_like(img, dtype=np.float64)
    img_back += img.astype(np.float64)
img_back = img_back / frame_count
img_back = img_back.astype(np.uint8)

# Save and show the background image
cv.imwrite('../data/PETS09-S2L1-raw_back.png', img_back)
cv.imshow('Background Extraction', img_back)
cv.waitKey()
cv.destroyAllWindows()
