import numpy as np
import cv2 as cv
from histogram import get_histogram, conv_hist2img

# Read the given image as gray scale
img = cv.imread('../data/baboon.tif', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# Initialize control parameters
value_range = [20, 200] # [lower limit, upper limit]

while True:
    # Apply contrast and brightness
    # Alternative) cv.intensity_transform.contrastStretching() (with s1=0 and s2=255)
    img_tran = 255 / (value_range[1] - value_range[0]) * (img.astype(np.int32) - value_range[0])
    img_tran = img_tran.astype(np.uint8) # Apply saturation

    # Get image histograms
    hist = conv_hist2img(get_histogram(img))
    hist_tran = conv_hist2img(get_histogram(img_tran))

    # Mark the intensity range, 'value_range'
    if value_range[0] >= 0 and value_range[0] <= 255:
        mark = hist[:, value_range[0]] == 255
        hist[mark, value_range[0]] = 200
    if value_range[1] >= 0 and value_range[1] <= 255:
        mark = hist[:, value_range[1]] == 255
        hist[mark, value_range[1]] = 100

    # Show all images
    row0 = np.hstack((img, img_tran))
    row1 = np.hstack((hist, hist_tran))
    row1 = cv.resize(row1, (row0.shape[1], 255))
    merge = np.vstack((row0, row1))
    cv.imshow('Contrast Stretching: Original | Stretching', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        value_range[0] += 1
    elif key == ord('-') or key == ord('_'):
        value_range[0] -= 1
    elif key == ord(']') or key == ord('}'):
        value_range[1] += 1
    elif key == ord('[') or key == ord('{'):
        value_range[1] -= 1

cv.destroyAllWindows()
