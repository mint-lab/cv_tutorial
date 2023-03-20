import numpy as np
import cv2 as cv

# Read the given video
video = cv.VideoCapture('data/PETS09-S2L1-raw.webm')
assert video.isOpened(), 'Cannot read the given video.'

frame_total = int(video.get(cv.CAP_PROP_FRAME_COUNT))
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
        print(f'Progress: {frame_count}/{frame_total}')

    # Add the image to the averaged image (the background image)
    # Alternative) cv.createBackgroundSubtractorMOG2(), cv::bgsegm
    if img_back is None:
        img_back = np.zeros_like(img, dtype=np.float64)
    img_back += img.astype(np.float64) / frame_total

# Adjust the weight if 'frame_total' and 'frame_count' is not same
if frame_total != frame_count:
    img_back = img_back * frame_count / frame_total

# Save and show the background image
img_back = img_back.astype(np.uint8)
cv.imwrite('data/PETS09-S2L1-raw_back.png', img_back)
cv.imshow('Background Extraction', img_back)
cv.waitKey()
cv.destroyAllWindows()
