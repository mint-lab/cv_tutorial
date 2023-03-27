import numpy as np
import cv2 as cv

# Read the given video
video = cv.VideoCapture('../data/PETS09-S2L1-raw.webm')
assert video.isOpened(), 'Cannot read the given video'

img_prev = None
while True:
    # Get an image from 'video'
    valid, img = video.read()
    if not valid:
        break

    # Get the image difference
    if img_prev is None:
        img_prev = img.copy()
        continue
    img_diff = np.abs(img.astype(np.int32) - img_prev).astype(np.uint8) # Alternative) cv.absdiff()
    img_prev = img.copy()

    # Show all images
    merge = np.hstack((img, img_diff))
    cv.imshow('Image Difference: Original | Difference', merge)

    # Process the key event
    key = cv.waitKey(1)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

cv.destroyAllWindows()
