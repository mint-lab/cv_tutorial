import numpy as np
import cv2 as cv

img_list = [
    '../data/lena.tif',
    '../data/baboon.tif',
    '../data/peppers.tif',
]

# Initialize a control parameter
img_select = 0

while True:
    # Read the given image
    img = cv.imread(img_list[img_select])
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # Apply histogram equalization to each channel
    img_hist1 = np.dstack((cv.equalizeHist(img[:,:,0]),
                           cv.equalizeHist(img[:,:,1]),
                           cv.equalizeHist(img[:,:,2])))

    # Apply histogram equalization only to the luminance channel in YCbCr
    img_cvt = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
    img_hist2 = np.dstack((cv.equalizeHist(img_cvt[:,:,0]),
                           img_cvt[:,:,1],
                           img_cvt[:,:,2]))
    img_hist2 = cv.cvtColor(img_hist2, cv.COLOR_YCrCb2BGR)

    # Show all images
    merge = np.hstack((img, img_hist1, img_hist2))
    cv.imshow('Color Histogram Equalization: Image | Each Channel | Luminance Channel', merge)
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
