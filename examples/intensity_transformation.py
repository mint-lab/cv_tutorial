import numpy as np
import cv2 as cv

# Read the given image as gray scale
img = cv.imread('../data/baboon.tif', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# Intialize control parameters
contrast = 1.6
contrast_step = 0.1
brightness = -40
brightness_step = 1

while True:
    # Apply contrast and brightness
    img_tran = contrast * img + brightness # Alternative) cv.equalizeHist(), cv.intensity_transform
    img_tran[img_tran < 0] = 0
    img_tran[img_tran > 255] = 255
    img_tran = img_tran.astype(np.uint8)   # Alternative) cv.convertScaleAbs() for the above 3 lines

    # Show all images
    info = f'Contrast: {contrast:.1f}, Brightness: {brightness:.0f}'
    cv.putText(img_tran, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 255, thickness=2)
    cv.putText(img_tran, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 0)
    merge = np.hstack((img, img_tran))
    cv.imshow('Intensity Transformation: Original | Contrast/Brightness', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        contrast += contrast_step
    elif key == ord('-') or key == ord('_'):
        contrast -= contrast_step
    elif key == ord(']') or key == ord('}'):
        brightness += brightness_step
    elif key == ord('[') or key == ord('{'):
        brightness -= brightness_step

cv.destroyAllWindows()
