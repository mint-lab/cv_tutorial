import numpy as np
import cv2 as cv

# Read the given video
video = cv.VideoCapture('../data/PETS09-S2L1-raw.webm')
assert video.isOpened(), 'Cannot read the given video'

# Initialize control parameters
blur_ksize = (9, 9)
blur_sigma = 3
diff_threshold = 50
bg_update_rate = 0.05
fg_update_rate = 0.001
zoom_level = 0.8

# Read the background image
img_back = cv.imread('../data/PETS09-S2L1-raw_back.png')
assert img_back is not None, 'Cannot read the initial background image'
img_back = cv.GaussianBlur(img_back, blur_ksize, blur_sigma).astype(np.float64)

box = lambda ksize: np.ones((ksize, ksize), dtype=np.uint8)
while True:
    # Get an image from 'video'
    valid, img = video.read()
    if not valid:
        break

    # Get the difference between the current image and background
    img_blur = cv.GaussianBlur(img, blur_ksize, blur_sigma)
    img_diff = img_blur - img_back

    # Apply thresholding
    img_norm = np.linalg.norm(img_diff, axis=2)
    img_bin = np.zeros_like(img_norm, dtype=np.uint8)
    img_bin[img_norm > diff_threshold] = 255

    # Apply morphological operations
    img_mask = img_bin.copy()
    img_mask = cv.erode(img_mask, box(3))               # Suppress small noise
    img_mask = cv.dilate(img_mask, box(5))              # Connect broken parts
    img_mask = cv.dilate(img_mask, box(3))              # Connect broken parts
    fg = img_mask == 255                                # Keep the (thick) foreground mask
    img_mask = cv.erode(img_mask, box(3), iterations=2) # Restore the thick mask thin

    # Update the background
    # Alternative) cv.createBackgroundSubtractorMOG2(), cv.bgsegm
    bg = ~fg
    img_back[bg] = (bg_update_rate * img_blur[bg] + (1 - bg_update_rate) * img_back[bg]) # With the higher weight
    img_back[fg] = (fg_update_rate * img_blur[fg] + (1 - fg_update_rate) * img_back[fg]) # With the lower weight

    # Get the foreground image
    img_fore = np.zeros_like(img)
    img_fore[fg] = img[fg]

    # Show all images
    merge = np.vstack((np.hstack((img, img_back.astype(np.uint8))),
                       np.hstack((cv.cvtColor(img_mask, cv.COLOR_GRAY2BGR), img_fore))))
    merge = cv.resize(merge, None, None, zoom_level, zoom_level)
    cv.imshow('Change Detection: Original | Background | Foreground Mask | Foreground', merge)

    # Process the key event
    key = cv.waitKey(1)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

cv.destroyAllWindows()
